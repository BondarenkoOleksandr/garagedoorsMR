from rest_framework import serializers

from states.models import State, FirstScreen, SecondScreen, ThirdScreen


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


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'


class StateDetailSerializer(serializers.ModelSerializer):
    firstscreen = FirstScreenSerializer()
    secondscreen = SecondScreenSerializer()
    thirdscreen = ThirdScreenSerializer()

    class Meta:
        model = State
        fields = '__all__'
