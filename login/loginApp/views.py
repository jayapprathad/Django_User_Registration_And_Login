#from imaplib import _Authenticator
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.

def signin(request):
    if request.method == 'POST':
        
        user=request.POST.get('user',False)
        password=request.POST.get('password')
        
        user1 =authenticate(username=user, password=password)
        
        if user1 is not None:
            login(request, user1)
            uname = user1.user
            #messages.success(request, "Logged In Sucessfully!!")
            
            return render(request, "loginApp/check.html",{'uname':uname})

        else:
            #messages.error(request,"Please check your Username or Password!!")   
            
            return render(request, "loginApp/test.html")
    
    return render(request, "loginApp/index.html")

# def check(request):
#     return render(request,"loginApp/check.html")


    
