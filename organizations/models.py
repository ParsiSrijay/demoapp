from django.db import models

# Create your models here.
class Addpolicy(models.Model):
    Policyname=models.CharField(max_length=20)
    Description=models.CharField(max_length=40)
    Question1=models.CharField(max_length=30)
    Question2=models.CharField(max_length=30)
    Question3=models.CharField(max_length=30)
    Question4=models.CharField(max_length=30)
    Question5=models.CharField(max_length=30)


class Addpolicy1(models.Model):
    Policyname=models.CharField(max_length=20)
    Description=models.CharField(max_length=40)
    Question1=models.CharField(max_length=30)
    Question2=models.CharField(max_length=30)
    Question3=models.CharField(max_length=30)
    Question4=models.CharField(max_length=30)
    Question5=models.CharField(max_length=30)