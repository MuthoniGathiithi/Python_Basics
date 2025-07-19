from django.db import models
class Student(models.Model):
  name=models.CharField(max_length=100)
  age=models.IntegerField(max_length=3)
  school=models.CharField(max_length=100)
