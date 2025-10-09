from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index_html'),
    path('demo.html', views.demo, name='demo'),
    path('archives.html', views.archives, name='archives'),
    path('blog.html', views.blog, name='blog'),
    path('single.html', views.single, name='single'),
    path('page.html', views.page, name='page'),
]
