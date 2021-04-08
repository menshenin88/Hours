from django.db import models
import datetime
from decimal import *
from contacts.models import contacts

class accounts(models.Model):
    user_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    birth_date = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_of_employment = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user_name

class time_tracker(models.Model):
    contact_name = models.ForeignKey(contacts,on_delete=models.DO_NOTHING)
    user_name = models.ForeignKey(accounts,on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    def get_time_diff(self):
        timediff = self.stop_time - self.start_time
        timediff = timediff.total_seconds()/3600
        return timediff
    def get_total_amount(self):
        timediff = self.stop_time - self.start_time
        timediff = timediff.total_seconds()/3600
        total_amount = timediff * float(self.rate)
        return Decimal(total_amount).quantize(Decimal(10) ** -2)
