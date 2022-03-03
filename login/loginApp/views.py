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


    
