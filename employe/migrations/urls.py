from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.list_emloyes, name='list_emloyes'),
]