from django.shortcuts import render
from django.db.models import F, fields, ExpressionWrapper, DecimalField, DateTimeField
from django.db.models.functions import ExtractHour

from .models import accounts, time_tracker

def index(request):
    listed_accounts = accounts.objects.all()

    context = {
        'accounts': listed_accounts
    }

    return render(request, 'accounts/accounts.html', context)

def overview(request):
    tracker = time_tracker.objects.all().annotate(
        total_time=ExpressionWrapper(F('stop_time') - F('start_time'), output_field=DateTimeField()),
        #hour=ExtractHour(ExpressionWrapper(F('stop_time') - F('start_time'), output_field=DateTimeField())),
        #total_amount=ExpressionWrapper(F('rate')*ExtractHour('total_time'), output_field=DecimalField())
    )

    context = {
        'time_tracker': tracker
    }

    return render(request, 'accounts/time_tracker.html', context)
