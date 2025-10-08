from django.shortcuts import render

def index(request):
    return render(request, 'cars/index.html')

def toyota(request):
    return render(request, 'cars/toyota.html')

def honda(request):
    return render(request, 'cars/honda.html')

def renault(request):
    return render(request, 'cars/renault.html')
