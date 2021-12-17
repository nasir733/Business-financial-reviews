from django.urls import path
from .views import *
app_name = 'business'
urlpatterns = [
    path('<str:name>/<int:page>/', dashboard, name='dashboard'),
    path('edit-profile/<str:name>/', EditProfile, name='edit_profile'),
    path('your-businesses/', YourBusiness, name='your_businesses'),

]
