from rest_framework import serializers

class InputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False, default='')
    last_name = serializers.CharField(required=False, default='')