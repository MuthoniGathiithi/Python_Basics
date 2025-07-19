from django.db import models
class Student(models.Model):
  name=models.CharField(max_length=100)
  age=models.IntegerField()
  school=models.CharField(max_length=100)

  course = models.ForeignKey('Course', on_delete=models.CASCADE)

class Course(models.Model):
  name=models.CharField(max_length=100)
  code=models.CharField(max_length=10)
  time=models.TimeField()
  
class Unit(models.Model):
  name=models.CharField(max_length=100)
  code=models.CharField(max_length=10)
  course = models.ForeignKey('Course', on_delete=models.CASCADE)