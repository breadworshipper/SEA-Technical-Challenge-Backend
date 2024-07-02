from django.urls import path, include
from . import views

urlpatterns = [
    path('branch/', views.branch_post, name='branch_post'),
    path('getbranch/', views.branch_get, name='branch_get')
]
