from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.


class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email']
    list_filter = ['user', 'name', 'email']
    search_fields = ['user', 'name', 'email']


admin.site.register(BusinessProfile, BusinessProfileAdmin)
