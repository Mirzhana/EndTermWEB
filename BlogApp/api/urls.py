from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/', views.ListPosts.as_view()),
    path('posts/<int:pk>/', views.DetailPosts.as_view()),
    path('/api/<int:pk>/', views.DetailPosts.as_view()),
    path('/api/', views.DetailPosts.as_view()),
]