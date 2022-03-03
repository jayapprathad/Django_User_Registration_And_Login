from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from signupApp.models import Customer
# Create your views here.


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        print(customer)

        if customer:
            if password == customer.pass1:
                return render(request, 'loginApp/check.html', {'uname': customer.fname})
            else:
                messages.error(request, "Invalid Username or Password!!")
                return HttpResponseRedirect('#')

        messages.error(request, "Invalid Username or Password!!")
        return HttpResponseRedirect('#')
    else:
        return render(request, 'loginApp/index.html')






   