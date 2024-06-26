from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=[(1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five")])
    