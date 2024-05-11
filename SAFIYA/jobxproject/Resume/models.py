from django.db import models

# Create your models here.
class clientDb(models.Model):
    name = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True,null=True)
    addrs = models.CharField(max_length=100,blank=True,null=True)
    resume = models.FileField(upload_to='resume')



