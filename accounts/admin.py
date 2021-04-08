from django.contrib import admin

from .models import accounts, time_tracker

class accountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'first_name', 'last_name', 'tel', 'birth_date', 'email', 'date_of_employment')
    list_display_links = ('id', 'user_name')
    search_fields = ('user_name', 'email')
    list_per_page = 25

admin.site.register(accounts, accountsAdmin)

class time_trackerAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_name', 'user_name', 'start_time', 'stop_time', 'rate')
    list_display_links = ('id', 'contact_name')
    search_fields = ('contact_name', 'user_name')
    list_per_page = 25



admin.site.register(time_tracker, time_trackerAdmin)
