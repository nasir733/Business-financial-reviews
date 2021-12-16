from django.urls import path
from .views import *
app_name = 'business'
urlpatterns = [
    path('', dashboard, name='dashboard'),
]
