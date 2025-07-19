from django.db import models
from django.contrib.auth.models import User  # This is the built-in User model

ROLE_CHOICES = (
    ('student', 'Student'),
    ('lecturer', 'Lecturer'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    school = models.CharField(max_length=100)
    course = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    department = models.CharField(max_length=100)

class Unit(models.Model):
  name=models.CharField(max_length=100)
  code=models.CharField(max_length=10)
  course = models.ForeignKey('Course', on_delete=models.CASCADE)
