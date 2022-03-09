from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from signupApp.models import Customer
from .forms import Myform
from django.contrib.auth.hashers import make_password, check_password
import datetime
# Create your views here.


def signin(request):

    form=Myform()
    global email,password,customer
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        #customer
        customer = Customer.get_customer_by_email(email)

        #verification = customer.is_verified()
        print(customer.verified)

        if customer:

            if customer.verified == 'True':
                print("inside true part")
                flag = check_password(password, customer.pass1)

                if not form.is_valid():
                    messages.error(request,"Invalid Captcha")
                    return HttpResponseRedirect('#')
                if flag:
                    customer.login_time=datetime.datetime.now()
                    customer.status="active"
                    customer.save()
                    return render(request, 'loginApp/check.html', {'uname': customer.fname})
                else:
                    messages.error(request, "Invalid mail or Password!!")
                    return HttpResponseRedirect('#')
            else:
                print("inside false part")
                messages.error(request, "User not verified!! Please check your mail and verify!")
                return HttpResponseRedirect('#')
        else:
            messages.error(request, "Invalid mail id")
            return HttpResponseRedirect('#')
    else:
        return render(request, 'loginApp/index.html', {"form": form})





def signout(request):
    customer.logout_time=datetime.datetime.now() 
    customer.status="inactive"
    customer.save()
    return render(request, 'homeApp/index.html')
