from django.urls import path, include
from . import views

urlpatterns = [
    path('review/', views.review_post, name='review_post'),
    path('review/<int:page_number>/', views.review_get, name='review_get')
]
