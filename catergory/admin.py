from django.contrib import admin
from .models import *
# Register your models here.


class CatergoryAdmin(admin.ModelAdmin):
    list_display = ['name']

    search_fields = ['name']


admin.site.register(Catergory, CatergoryAdmin)
