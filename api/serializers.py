from rest_framework.serializers import ModelSerializer
from catergory.models import Catergory
from companydashboard.models import BusinessProfile
class CatergorySerializer(ModelSerializer):
    class Meta:
        model = Catergory
        fields = '__all__'
        
class BusinessSerializer(ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = '__all__'