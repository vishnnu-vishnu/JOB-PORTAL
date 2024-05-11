from django.db import models


# Create your models here.
class categorydb(models.Model):
    profile=models.ImageField(upload_to='cart',null=True,blank=True)
    company_id=models.EmailField(null=True)
    comapnyname=models.CharField(max_length=50,null=True)
    jobname = models.CharField(max_length=50,blank=True,null=True)
    jobexperience = models.CharField(max_length=50,blank=True)
    jobtype = models.CharField(max_length=50, blank=True, null=True)
    joblocation = models.CharField(max_length=50,blank=True)
    jobdes=models.CharField(max_length=50,blank=True,null=True)
    skills=models.CharField(max_length=50,blank=True,null=True)
    qualification=models.CharField(max_length=50,blank=True,null=True)
    lpa=models.CharField(max_length=50,blank=True,null=True)
    posted=models.DateField(auto_now=True)
class companyDb(models.Model):
    companyname = models.CharField(max_length=50, blank=True,null=True)
    email=models.EmailField(max_length=50,blank=True,null=True,unique=True)
    password=models.CharField(max_length=50,blank=True,null=True)
    mobile=models.IntegerField(max_length=50,null=True,blank=True)
    location = models.CharField(max_length=50, blank=True,null=True)
    state = models.CharField(max_length=50, blank=True,null=True)
    description = models.CharField(max_length=50, blank=True,null=True,default="Add Details")
    profile=models.ImageField(blank=True,null=True)


