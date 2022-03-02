#from imaplib import _Authenticator
from django.shortcuts import redirect, render
from django.contrib import messages
from signupApp.models import Customer
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_username(username)
        #customer = Customer.get_customer_by_password(password)
        error_message = None
        if customer:
            flag = check_password(password, customer.pass1)
            if flag:
                return render(request,'loginApp/check.html',{'uname':customer.username})
            else:
                error_message = 'username or password invalid !!'
                return render(request,'loginApp/test.html', {'error': error_message})

        else:
            error_message = 'username not exist!!'
            return render(request,'loginApp/test.html', {'error': error_message})
    else:
        return render(request,'loginApp/index.html')






    # user=request.POST.get('user',False)
        # password=request.POST.get('password')
        
        # user1 =authenticate(username=user, password=password)
        
        # if user1 is not None:
            # login(request, user1)
            # uname = user1.user
            #messages.success(request, "Logged In Sucessfully!!")
            
            # return render(request, "loginApp/check.html",{'uname':uname})

        # else:
            #messages.error(request,"Please check your Username or Password!!")   
            
            # return render(request, "loginApp/test.html")
    
    # return render(request, "loginApp/index.html")

# def check(request):
#     return render(request,"loginApp/check.html")


    
