from rest_framework import serializers
from .models import Pass, User, Coordinates, Level, Image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['fam', 'name', 'otc', 'email', 'phone']

class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ['latitude', 'longitude', 'height']

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['data', 'title']

class PassSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordinatesSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Pass
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'user', 'coords', 'level', 'images']
