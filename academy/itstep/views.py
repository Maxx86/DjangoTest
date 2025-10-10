from django.shortcuts import render
from .models import Teacher, Course, Student


def base(request):
    return render(request, 'base.html')


def teachers(request):
    teachers_list = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers_list})


def courses(request):
    courses_list = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses_list})


def students(request):
    students_list = Student.objects.all()
    return render(request, 'students.html', {'students': students_list})


def teachers_view(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def courses_view(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def students_view(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})