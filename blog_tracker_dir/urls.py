"""Defines URL patterns for blog_tracker_dir."""

from django.urls import path 

from . import views 

app_name = 'blog_tracker_dir'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics pages
    path('topics/', views.topics, name='topics'),
    # Details for single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]