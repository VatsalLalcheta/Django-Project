from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('edit/<str:R_name>', views.edit, name='edit'),
]
