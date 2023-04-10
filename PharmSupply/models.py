from django.db import models
from django.contrib.auth.models import User
from crequest.middleware import CrequestMiddleware
current_request = CrequestMiddleware.get_request(User)

# Create your models here.
# class Register(models.Model):
#     first_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)
#     phone = models.CharField(max_length=10)
#     gender=models.CharField(max_length=100)
#     email=models.CharField(max_length=100)
#     password1=models.CharField(max_length=100)
#     password2=models.CharField(max_length=100)
    

class Image(models.Model):
    # name = models.CharField(max_length=100)
    # age = models.CharField(max_length=100)
    # docname = models.CharField(max_length=100) 
    # medicines=models.CharField(max_length=100)
    caption = models.CharField(max_length=100) 
    image=models.ImageField(upload_to="pers/%y") 
    def __str__(self): 
        return self.caption 
# Create your models here.

class order(models.Model):
    #uid=models.ForeignKey(User, on_delete=models.CASCADE, default=current_request)
    # id = models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE, default=current_request)
    oid = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='pending')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    medi1=models.CharField(max_length=100)
    quantity1=models.CharField(max_length=100)
    medi2=models.CharField(max_length=100, blank=True)
    quantity2=models.CharField(max_length=100, blank=True)
    medi3=models.CharField(max_length=100, blank=True)
    quantity3=models.CharField(max_length=100, blank=True)
    prescription=models.ImageField(upload_to="perscriptions", blank=True) 

    def __str__(self):
        return self.oid

class restricted(models.Model):
    mid = models.CharField(max_length=100)
    medicine=models.CharField(max_length=100)

    def __str__(self):
        return self.medicine

class bid(models.Model):
    bid = models.AutoField(primary_key=True)
    bid_price = models.CharField(max_length=100)
    bid_date = models.DateTimeField(auto_now_add=True)
    bid_status = models.CharField(max_length=10, default='pending')

    def __str__(self):
        return self.bid