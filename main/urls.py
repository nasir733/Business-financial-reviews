from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage, name='home'),
    path('businesslist/<str:catergory>/', BusinessList, name='businesslist'),
    path('business/<str:business_id>/<int:page>/',
         BusinessSingle, name='business'),
    path('catergories/', allcatergories, name='catergories'),

]
