from django.db import models

# Create your models here.
class contactdb(models.Model):
    message=models.CharField(max_length=500,null=True,blank=True)
    name = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(max_length=20,blank=True,null=True)
    subject = models.CharField(max_length=20,blank=True,null=True)

class registerdb(models.Model):
    name = models.CharField(max_length=500,null=True,blank=True)
    email = models.EmailField(max_length=20, blank=True, null=True)
    mobile = models.IntegerField( blank=True, null=True)
    resume = models.FileField( blank=True, null=True)
    profile = models.ImageField(blank=True, null=True)
    password = models.EmailField(max_length=20, blank=True, null=True)
    age=models.IntegerField(null=True,blank=True,default="0")
    dob=models.CharField(max_length=20,null=True,blank=True,default="Update Date Of Birth")
    sex=models.CharField(max_length=20,null=True,blank=True,default="Update sex")
    address=models.CharField(max_length=20,null=True,blank=True,default="Update Address")


class applicationdb(models.Model):
    job=models.CharField(max_length=100,null=True,blank=True)
    company=models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    resume=models.FileField(null=True,blank=True)
    reply=models.CharField(max_length=500,null=True,blank=True,default="No Reply")


