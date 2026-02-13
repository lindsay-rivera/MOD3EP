from django.db import models
from django.utils import timezone


# Create your models here.
class Supplier(models.Model):

    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    created_at = models.DateTimeField(blank=True, null = True)
    objects = models.Manager()
    
    def getName(self):
        return self.name

    def __str__(self):
        return f"{self.name}, {self.city}, {self.country} (created at: {self.created_at})"