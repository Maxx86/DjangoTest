from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('helloweb.urls')),
    # path('', include('blog.urls')),
    # path('', include('sports.urls')),
    # path('', include('cars.urls')),
    path('', include('weekdays.urls')),
]
