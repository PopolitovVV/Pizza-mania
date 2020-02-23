from django.urls import path, include
from django.contrib import admin

from landing import views

urlpatterns = [
    path('', views.home, name='home'),
    path('landing/', views.landing, name='landing'),
]
