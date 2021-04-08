from django.db import models
from datetime import datetime

class contacts(models.Model):
    contact_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.contact_name
# Create your models here.
