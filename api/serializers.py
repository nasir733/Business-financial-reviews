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
        
    def create(self,validated_data):
        category = Catergory.objects.get(name=validated_data['catergory'].name)
        business = BusinessProfile.objects.create(**validated_data, catergory=category)
        return business
        