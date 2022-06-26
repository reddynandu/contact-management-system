from django.db import models

class Information(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    lname= models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phoneNumber = models.CharField(max_length=10)
