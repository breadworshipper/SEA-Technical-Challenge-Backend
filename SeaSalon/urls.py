"""
URL configuration for SeaSalon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

# Define your API v1 patterns here
patterns = [
    path('', include('reservation.urls')), 
    path('', include('review.urls')), 
    path('', include('authentication.urls')),
    path('', include('branch.urls')),
]

urlpatterns = [
    path('api/v1/', include(patterns)),  # Include your API v1 patterns under the 'api/v1/' prefix
]
