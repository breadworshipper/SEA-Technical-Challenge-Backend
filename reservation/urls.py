from django.urls import path, include
from . import views

urlpatterns = [
    path('reservation/', views.reservation_post, name='reservation'),
    path('getreservation/', views.reservation_get, name='reservation_get')
]
