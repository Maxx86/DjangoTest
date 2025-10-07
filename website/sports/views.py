from django.shortcuts import render

def index(request):
    return render(request, 'sports/index.html')

def football(request):
    return render(request, 'sports/football.html')

def hockey(request):
    return render(request, 'sports/hockey.html')

def basketball(request):
    return render(request, 'sports/basketball.html')
