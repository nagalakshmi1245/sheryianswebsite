from django.db import models

# Create your models here.
class request(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    date=models.DateTimeField(auto_now_add=False)
    enquiry=models.CharField(max_length=20)

class courses(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    language=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')

class loginModel(models.Model):
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=50)
    