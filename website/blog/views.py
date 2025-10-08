from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.views.generic import CreateView

from .forms import PostForm
from .models import Post, Category


def get_categories():
    all = Category.objects.all()
    half = all.count() // 2
    first_half = all[:half]
    second_half = all[half:]
    return {'cats1': first_half,
            'cats2': second_half}


def index(request):
    posts = Post.objects.all().order_by("-published_date")
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts, 'page_obj': page_obj}
    context.update(get_categories())
    return render(request, "blog/index.html", context=context)


def about(request):
    context = {}
    return render(request, "blog/about.html", context=context)


def contact(request):
    context = {}
    return render(request, "blog/contact.html", context=context)


def post(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    context.update(get_categories())
    return render(request, "blog/post.html", context=context)


def category(request, slug=None):
    c = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=c).order_by("-published_date")
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context=context)


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query)).order_by("-published_date")
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts, 'page_obj': page_obj}
    context.update(get_categories())
    return render(request, "blog/index.html", context=context)


# @login_required
# def create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.published_date = now()
#             post.auther = request.user
#             post.save()
#     formCreate = PostForm()
#     context = {'formCreate': formCreate}
#     context.update(get_categories())
#     return render(request, "blog/create.html", context=context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/create.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.published_date = now()
        post.auther = self.request.user
        post.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_categories())

        return context


def custom_logout_view(request):
    logout(request)
    return redirect('home')
