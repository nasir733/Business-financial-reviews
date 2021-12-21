from rest_framework.serializers import ModelSerializer
from catergory.models import Catergory
from companydashboard.models import BusinessProfile
class CatergorySerializer(ModelSerializer):
    class Meta:
        model = Catergory
        fields = '__all__'
        
class BusinessSerializer(ModelSerializer):
    catergory = CatergorySerializer(many=False, read_only=True)
    class Meta:
        model = BusinessProfile
        exclude = ('id',)
        read_only_fields =('catergory')