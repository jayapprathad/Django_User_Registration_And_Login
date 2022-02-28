#from typing_extensions import Self
from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    pass1 = models.CharField(max_length=500)
    pass2 = models.CharField(max_length=500, default=pass1)
    phonenumber =  models.CharField(max_length=15)

    def register(self):
        self.save()

    def usernameisExist(self):
         if Customer.objects.filter(username=self.username).exists():
            return True
         else:
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



