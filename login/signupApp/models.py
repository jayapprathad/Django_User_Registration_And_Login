from django.db import models

# Create your models here.
class Customer(models.Model):
    fname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(null=True, max_length=50)
    email = models.EmailField(null=True, max_length=255)
    pass1 = models.CharField(null=True, max_length=20)
    login_time =  models.DateTimeField(null=True)
    logout_time = models.DateTimeField(null=True)
    status =  models.CharField(null=True, max_length=20)
    verified =  models.CharField(null=True, max_length=20)
    

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

