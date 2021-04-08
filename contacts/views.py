from django.shortcuts import render

from .models import contacts

def index(request):
  listed_contacts = contacts.objects.all()

  context = {
    'contacts': listed_contacts
  }

  return render(request, 'contacts/contacts.html', context)
