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
        fields = '__all__'
        
    def create(self,validated_data):
        category = Catergory.objects.filter(name=validated_data['catergory'].name).exists()
        if category:
            business = BusinessProfile.objects.create(**validated_data, catergory=category)
        business = BusinessProfile.objects.create(**validated_data)
        return business
        