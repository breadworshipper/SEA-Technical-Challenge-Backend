from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=[1, 2, 3, 4, 5])
    