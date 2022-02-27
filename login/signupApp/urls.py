from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .import views

urlpatterns = [
    #path('signup', views.signup,name="signup"),
    #path('signup/', views.signup),
    path('index.html/', views.signup),
    path('activate/<uidb64>/<token>', views.activate, name="activate")
    
]