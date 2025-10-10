from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('teachers/', views.teachers, name='teachers'),
    path('courses/', views.courses, name='courses'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers_view, name='teachers'),
    path('courses/', views.courses_view, name='courses'),
    path('students/', views.students_view, name='students'),
]
