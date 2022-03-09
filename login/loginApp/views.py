from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from signupApp.models import Customer
from .forms import Myform
from django.contrib.auth.hashers import check_password
import datetime
# Create your views here.


def signin(request):

    global customer

    cap=Myform(request.POST)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        if customer:

            if customer.verified == 'True':
                flag = check_password(password, customer.pass1)
                
                if flag:
                    if cap.is_valid():
                        customer.login_time=datetime.datetime.now()
                        customer.status="active"
                        customer.save()
                        return render(request, 'loginApp/check.html', {'uname': customer.fname})
                    else:
                        messages.error(request,"Invalid Captcha")
                        return HttpResponseRedirect('#')
                else:
                    messages.error(request, "Invalid email or Password!!")
                    return HttpResponseRedirect('#')
            else:
                 messages.error(request, "User not verified!! Please check your mail and verify!")
                 return HttpResponseRedirect('#')
        else:
            messages.error(request, "Invalid email!")
            return HttpResponseRedirect('#')
    else:
        return render(request, 'loginApp/index.html', {"cap": cap})


def signout(request):
    customer.logout_time=datetime.datetime.now() 
    customer.status="inactive"
    customer.save()
    return redirect('homepage')
