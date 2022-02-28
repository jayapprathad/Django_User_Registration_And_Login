#from imaplib import _Authenticator
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.contrib import messages

from signupApp.models import Customer





# Create your views here.

def signin(request):
    if request.method == 'POST':
        
        username=request.POST.get('username')  
        pass1=request.POST.get('pass1')
        #Code commented below- Swa
        #customuser=Customer(username=username,pass1=pass1)
        #user1 =authenticate(username=customuser.username, password=customuser.pass1)
        #END Code commented - Swa
        user1 =authenticate(username=username, password=pass1)
        #Code added below- Swa
        #END Code added - Swa
        #user = _Authenticator(username=username, pass1=pass1)
        #print(user.username)
        if user1 is not None:
            login(request, user1)
            uname = user1.username
            print(uname)
            #messages.success(request, "Logged In Sucessfully!!")
            #return render(request, "authentication/index.html",{"fname":fname})
            return render(request, "loginApp/check.html",{'uname':uname})
            #return render(request, "homeApp/index.html",{'uname':uname})
            #return render(request, "loginApp/index.html")

        else:
            print("checking")
            messages.error(request,"Please check your Username or Password!!")   
            #return redirect('home')
            #return render(request,"homeApp/index.html")
            return render(request, "loginApp/check.html")
            #return render(request, "loginApp/test.html")
            #return render(request, "loginApp/index.html")
    
    return render(request, "loginApp/index.html")

def check(request):
    return render(request,"loginApp/check.html")




    
