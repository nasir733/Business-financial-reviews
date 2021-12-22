from rest_framework.serializers import ModelSerializer
from catergory.models import Catergory
from companydashboard.models import BusinessProfile


class CatergorySerializer(ModelSerializer):
    class Meta:
        model = Catergory
        fields = '__all__'


class BusinessSerializer(ModelSerializer):
    catergory = CatergorySerializer(many=False, read_only=False)

    class Meta:
        model = BusinessProfile
        fields = '__all__'

    # def create(self, validated_data):
    #     print(validated_data.get('catergory').get('name'))
    #     categoryName = str(validated_data.get('catergory').get('name'))
    #     del validated_data['catergory']

    #     if Catergory.objects.filter(name=categoryName).exists():
    #         category = Catergory.objects.filter(name=categoryName).first()
    #         print('category found')
    #         business = BusinessProfile.objects.create(
    #             **validated_data, catergory=category)
    #         return business

    #     else:
    #         categoryCreate = Catergory.objects.create(
    #             name=categoryName)
    #         business = BusinessProfile.objects.create(
    #             **validated_data, catergory=categoryName)
    #         print('business created')
    #         return business
