from django.db import models

# Create your models here.

class Contact(models.Model):
    userID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    query = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add = True)