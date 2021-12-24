from django.contrib import admin
from .models import *
# Register your mfdels here.

from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'business', 'rating']

    search_fields = ['review', 'rating', 'user']


class ReviewCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'review']

    search_fields = ['review', 'comment', 'user']


admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewComment, ReviewCommentAdmin)
