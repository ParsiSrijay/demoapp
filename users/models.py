from django.db import models

# Create your models here.

class userresponse(models.Model):
    Policyname=models.CharField(max_length=20)
    Question1=models.CharField(max_length=30)
    Question2=models.CharField(max_length=30)
    Question3=models.CharField(max_length=30)
    Question4=models.CharField(max_length=30)
    Question5=models.CharField(max_length=30)


class userresponse1(models.Model):
    Policyname=models.CharField(max_length=20)
    Question1=models.CharField(max_length=30)
    Question2=models.CharField(max_length=30)
    Question3=models.CharField(max_length=30)
    Question4=models.CharField(max_length=30)
    Question5=models.CharField(max_length=30)