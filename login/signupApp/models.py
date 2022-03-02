#from typing_extensions import Self
from django.db import models


# Create your models here.
class Customer(models.Model):
    fname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(null=True, max_length=50)
    email = models.EmailField(null=True, max_length=255)
    pass1 = models.CharField(null=True, max_length=500)
    pass2 = models.CharField(null=True, max_length=500, default=pass1)

    def register(self):
        self.save()

    def usernameisExist(self):
        if Customer.objects.filter(username=self.username):
            print('true')
            return True
        else:
            print('false')
            return False

    def mailisExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_customer_by_username(username):
        try:
            return Customer.objects.get(username=username)
        except:
            return False

    @staticmethod
    def get_customer_by_password(password):
        try:
            return Customer.objects.get(pass1=password)
        except:
            return False
