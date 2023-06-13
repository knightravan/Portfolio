from django.db import models

# Create your models here.
class contact(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField()
	sub=models.CharField(max_length=100)
	message=models.TextField()

class act(models.Model):
	name32=models.CharField(max_length=30)
	email32=models.EmailField()
	sub32=models.CharField(max_length=100)
	message32=models.TextField()