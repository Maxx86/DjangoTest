from django.shortcuts import render, get_object_or_404

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
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context=context)


def search(request):
    posts = Post.objects.all().order_by("-published_date")
    context = {'posts': posts}
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
