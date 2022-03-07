from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from signupApp.models import Customer
import random 
from .forms import Myform
# Create your views here.


def signin(request):

    form=Myform()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)

        if customer:
            if not form.is_valid():
                messages.error(request,"Invalid Captcha")
            if password == customer.pass1:
                return render(request, 'loginApp/check.html', {'uname': customer.fname})
            else:
                messages.error(request, "Invalid Username or Password!!")
                return HttpResponseRedirect('#')

        messages.error(request, "Invalid Username or Password!!")
        return HttpResponseRedirect('#')
    else:
        return render(request, 'loginApp/index.html',{"form":form})