from rest_framework.serializers import ModelSerializer

from web.models import Material, UserProfile


class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
