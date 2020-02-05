from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('details/<str:R_name>/<str:U_name>', views.details, name='details'),
]
