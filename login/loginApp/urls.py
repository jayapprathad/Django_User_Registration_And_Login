from django.urls import path
from . import views

urlpatterns = [
    #path('check.html/', views.signin),
    path('index.html/', views.signin),
]