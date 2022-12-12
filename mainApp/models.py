from django.db import models
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
class mashalachicken(models.Model):
	half = models.IntegerField()
	full = models.IntegerField()
class tavadhosa(models.Model):
	masaladhosa = models.IntegerField()
	paneerdhosa = models.IntegerField()

# Create your models here.
