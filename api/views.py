from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
# Create your views here.
from rest_framework import viewsets
from catergory.models import Catergory
from companydashboard.models import BusinessProfile
from users.models import CustomUser
from rest_framework.response import Response
from rest_framework import status


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Catergory.objects.all()
    serializer_class = CatergorySerializer
    permission_classes = []


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = []


class BusinessApiView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        categoryName = request.data.get('catergory').get('name')
        name = request.data.get('name')
        description = request.data.get('description')
        email = request.data.get('email')
        phone = request.data.get('phone')
        address = request.data.get('address')
        website = request.data.get('website')
        facebook = request.data.get('facebook')
        twitter = request.data.get('twitter')
        instagram = request.data.get('instagram')
        image = request.data.get('image')
        avg_rating = request.data.get('avg_rating')
        employee_count = request.data.get('employee_count')
        city = request.data.get('city')
        country = request.data.get('country')
        postal_code = request.data.get('postal_code')
        score = request.data.get('score')
        sales = request.data.get('sales')
        user = CustomUser.objects.get(id=request.data.get('user'))
        state = request.data.get('state')
        catergory = Catergory.objects.filter(name=categoryName).first()
        lead = BusinessProfile.objects.filter(catergory=catergory, name=name, description=description, email=email, phone=phone, address=address, website=website, facebook=facebook, twitter=twitter,
                                              instagram=instagram, image=image, avg_rating=avg_rating, employee_count=employee_count, city=city, country=country, postal_code=postal_code, score=score, sales=sales, state=state, user=user).exists
        if not lead:
            if Catergory.objects.filter(name=categoryName).exists():
                print('Inside If Statement')
                lead = BusinessProfile.objects.create(catergory=catergory, name=name, description=description, email=email, phone=phone,    address=address, website=website, facebook=facebook, twitter=twitter,
                                                      instagram=instagram, image=image, avg_rating=avg_rating, employee_count=employee_count, city=city, country=country, postal_code=postal_code, score=score, sales=sales, state=state, user=user)
                lead.save()
                print('lead is saved ')
            else:
                print('Inside Else Statement')
                createNewCategory = Catergory.objects.create(
                    name=categoryName, description=description, image=image)
                lead = BusinessProfile.objects.create(catergory=createNewCategory, name=name, description=description, email=email, phone=phone,    address=address, website=website, facebook=facebook, twitter=twitter,
                                                      instagram=instagram, image=image, avg_rating=avg_rating, employee_count=employee_count, city=city, country=country, postal_code=postal_code, score=score, sales=sales, state=state, user=user)
                lead.save()
            return Response({'message': 'Lead created successfully', 'lead': lead.name}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Lead already exists'}, status=status.HTTP_400_BAD_REQUEST)
