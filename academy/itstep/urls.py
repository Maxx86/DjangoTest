from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('teachers/', views.teachers, name='teachers'),
    path('courses/', views.courses, name='courses'),
    path('students/', views.students, name='students'),
]
