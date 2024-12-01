from django.db import models


class User(models.Model):
    first_name=models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField( max_length=40)
    phone = models.CharField(max_length=10)
    address =models.CharField(max_length=500)
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=20)
    
class Services(models.Model):
    choices = [
        ("gas refill", "Gas Refill"),
        ("gas fitting","Gas Fitting"),
        ("other","Other")
    ]
    
    file = models.FileField( upload_to="service_requests_files/")
    service_type = models.CharField(choices=choices, max_length=1000)
    description = models.TextField()
    username = models.CharField( max_length=15)
    status = models.CharField( max_length=50,default="Pending")
    