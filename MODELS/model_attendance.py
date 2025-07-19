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



#session models 

from django.db import models
from django.utils import timezone
from accounts.models import Unit, Profile
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

class Session(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'role': 'lecturer'})
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Auto-generate a QR code using unit code and date
        qr_data = f"{self.unit.code}_{self.date}"
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer)
        filename = f"{self.unit.code}_{self.date}.png"
        self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.unit.name} - {self.date} ({self.start_time}-{self.end_time})"

