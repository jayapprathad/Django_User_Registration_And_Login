#from typing_extensions import Self
from login import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import login
from . tokens import generate_token
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
                request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

            # Welcome Email
            subject = "Welcome to our website!!"

            message = "Hello " + str(myuser.fname) + "!! \n" + \
                      "Welcome to our website! \nThank you for visiting us.\n \n\nThanking You\n Team SASTRA"

            from_email = settings.EMAIL_HOST_USER
            to_list = [myuser.email]
            send_mail(subject, message, from_email,
                      to_list, fail_silently=True)

            # Email Address Confirmation Email
            current_site = get_current_site(request)
            email_subject = "Confirm your Email - Django Login!!"
            message2 = render_to_string('signupApp/email_confirmation.html', {
                'name': myuser.fname,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                'token': generate_token.make_token(myuser)
            })

        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        return redirect('homepage')
    else:
        return render(request, 'signupApp/index.html')



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('loginApp/index.html')
    else:
        return render(request, 'signupApp/activation_failed.html')