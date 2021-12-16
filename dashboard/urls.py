from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='dashboard'),
    path('edit-profile/', EditProfile, name='edit_profile'),
]
