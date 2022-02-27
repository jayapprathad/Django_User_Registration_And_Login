from imaplib import _Authenticator
from pyexpat.errors import messages
from django.shortcuts import redirect, render

# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = _Authenticator(username=username, password=pass1)
        
        if user is not None:
            signin(request, user)
            uname = user.username
            # messages.success(request, "Logged In Sucessfully!!")
            #return render(request, "authentication/index.html",{"fname":fname})
            return render(request, "loginApp/check.html",{'uname':uname})
        else:

            messages="pls check your credentials"
            #messages.error(request,"Please check your Username or Password")
            return render(request,"loginApp/index.html",{'error':messages})
            #messages.error(request, "Bad Credentials!!")
            #return redirect('home')
    
    return render(request, "loginApp/index.html")

def check(request):
    return render(request,"loginApp/check.html")




    
