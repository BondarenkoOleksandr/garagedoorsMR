from rest_framework import serializers

from states.models import State, FirstScreen, SecondScreen, ThirdScreen


class FirstScreenStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstScreen
        fields = '__all__'


class SecondScreenStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondScreen
        fields = '__all__'


class ThirdScreenStateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='image.image', allow_null=True)

    class Meta:
        model = ThirdScreen
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'


class StateDetailSerializer(serializers.ModelSerializer):
    firstscreen = FirstScreenStateSerializer()
    secondscreen = SecondScreenStateSerializer()
    thirdscreen = ThirdScreenStateSerializer()

    class Meta:
        model = State
        fields = '__all__'
