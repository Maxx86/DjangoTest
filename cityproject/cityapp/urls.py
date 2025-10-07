from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),
    path('facts/', views.facts, name='facts'),
    path('contacts/', views.contacts, name='contacts'),
    path('history/', views.history, name='history'),
    path('history/people/', views.history_people, name='history_people'),
    path('history/photos/', views.history_photos, name='history_photos'),
]
