from django.shortcuts import render
from .serializers import *
# Create your views here.
from rest_framework import viewsets
from catergory.models import Catergory
from companydashboard.models import BusinessProfile
class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Catergory.objects.all()
    serializer_class = CatergorySerializer
    permission_classes = []

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = []
