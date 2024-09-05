"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # A page that displays all topics
    path('topics/', views.topics, name='topics'),
    # A page dedicated to a particular topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # A page for adding a new topic
    path('new_topic', views.new_topic, name='new_topic'),
    # A page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # A page for editing an existing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
