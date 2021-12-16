from django.urls import path
from .views import *
app_name = 'business'
urlpatterns = [
    path('<int:page>/', dashboard, name='dashboard'),
    path('edit-profile/', EditProfile, name='edit_profile'),

]
