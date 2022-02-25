from django.urls import path
from django.contrib import admin
from django.urls import path, include
from .import settings
from .import views

urlpatterns = [
    path('index.html/', views.signup)
    path('activate/<uidb64>/<token>', views.activate, name="activate")
    
]