from login import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .models import Customer

# Create your views here.


def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = Customer(fname=fname, lname=lname, username=username, email=email,
                          pass1=pass1, pass2=pass2)

        # validation

        if myuser.usernameisExist():
            messages.error(request, "Username Already Registered!!")
            return HttpResponseRedirect('#')

        if myuser.mailisExist():
            messages.error(request, "Email Already Registered!!")
            return HttpResponseRedirect('#')

        if myuser.pass1 != myuser.pass2:
            messages.error(request, "Passwords didn't matched!!")
            return HttpResponseRedirect('#')

        else:
            myuser.is_active = False
            myuser.register()

            messages.success(
                request, "Your Account has been created succesfully!! Please check your email to confirm your email address.")

            # Welcome Email
            subject = "Welcome to our website!!"

            message = "Hello " + str(myuser.fname) + "!! \n" + \
                      "Welcome to our website! \nThank you for visiting us.\n \n\nThanking You\n Team SASTRA"

            from_email = settings.EMAIL_HOST_USER
            to_list = [myuser.email]
            send_mail(subject, message, from_email,
                      to_list, fail_silently=True)

        return redirect('homepage')
    else:
        return render(request, 'signupApp/index.html')
