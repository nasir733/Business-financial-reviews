from django.urls import path
from .views import *


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('create-your-business/', businessregister, name='business-register'),


]
