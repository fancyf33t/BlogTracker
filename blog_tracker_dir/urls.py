"""Defines URL patterns for blog_tracker_dir."""

from django.urls import path 

from . import views 

app_name = 'blog_tracker_dir'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]