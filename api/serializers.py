from rest_framework.serializers import ModelSerializer
from catergory.models import Catergory
from companydashboard.models import BusinessProfile
class CatergorySerializer(ModelSerializer):
    class Meta:
        model = Catergory
        fields = '__all__'
        
class BusinessSerializer(ModelSerializer):
    category = CatergorySerializer(many=False, read_only=True)
    class Meta:
        model = BusinessProfile
        fields = '__all__'