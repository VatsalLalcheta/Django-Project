from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('feed', views.feed, name='feed'),
    path('add', views.add, name='add'),
    path('search', views.search, name='search'),
]
