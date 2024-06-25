from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    type_of_service = models.CharField(max_length=100, choices=[
        ('Haircuts and styling', 'haircuts and styling'),
        ('Manicure and pedicure', 'manicure and pedicure'),
        ('Facial treatment', 'facial treatment'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField()
    