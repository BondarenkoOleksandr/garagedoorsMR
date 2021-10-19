from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')
    state = serializers.CharField(source='state.name')
    date = serializers.DateField(format="%d %b %Y")

    class Meta:
        model = Review
        fields = '__all__'
