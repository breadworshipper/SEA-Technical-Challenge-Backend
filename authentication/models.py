from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=100, choices=[
        ('Customer', 'customer'),
        ('Admin', 'admin'),
    ], default='Customer')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number']

    def save(self, *args, **kwargs):
        # Automatically populate the username field with the email's local-part
        self.username = self.email
        super(CustomUser, self).save(*args, **kwargs)