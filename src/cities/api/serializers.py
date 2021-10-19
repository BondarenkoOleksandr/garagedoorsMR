from rest_framework import serializers

from cities.models import City, FirstScreen, SecondScreen, ThirdScreen


class FirstScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstScreen
        fields = '__all__'


class SecondScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondScreen
        fields = '__all__'


class ThirdScreenSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='image.image', allow_null=True)

    class Meta:
        model = ThirdScreen
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class CityDetailSerializer(serializers.ModelSerializer):
    firstscreen = FirstScreenSerializer()
    secondscreen = SecondScreenSerializer()
    thirdscreen = ThirdScreenSerializer()

    class Meta:
        model = City
        fields = '__all__'
