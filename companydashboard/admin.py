from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.


class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'user',  'email']
    list_filter = ['name', 'user',  'email']
    search_fields = ['name', 'user',  'email']


admin.site.register(BusinessProfile, BusinessProfileAdmin)
