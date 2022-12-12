from django.db import models

# Create your models here.
class Addstudent(models.Model):
    name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    instagram_link = models.URLField( max_length=200)