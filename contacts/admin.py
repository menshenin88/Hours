from django.contrib import admin

from .models import contacts

class contactsAdmin(admin.ModelAdmin):
  list_display = ('id', 'contact_name', 'address', 'city', 'tel', 'zipcode', 'email', 'contact_date' )
  list_display_links = ('id', 'contact_name')
  search_fields = ('contact_name', 'email')
  list_per_page = 25

admin.site.register(contacts, contactsAdmin)
