from django.urls import path
from . import views

app_name='signupApp'

urlpatterns = [
    path('index.html/', views.signup, name='signup'),
    path('index.html/', views.signup, name='signout')
]
    

