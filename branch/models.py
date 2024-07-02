from django.db import models

# Create your models here.
class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    open_time = models.TimeField()
    close_time = models.TimeField()

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
