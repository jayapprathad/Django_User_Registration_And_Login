from django.urls import path
from . import views

my_app='loginApp'

urlpatterns = [
    path('index.html/', views.signin,name="signin"),
]