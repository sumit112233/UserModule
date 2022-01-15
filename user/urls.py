from django.contrib import admin
from django.urls import path, include
from .views import HomeView, user_create,all_post, Post_create


urlpatterns = [
    path('/post',Post_create , name='post'),
    path('/allpost',all_post , name='all-post'),
    path('/user', user_create, name='user'),
    path('',HomeView.as_view(), name='home'),


]
