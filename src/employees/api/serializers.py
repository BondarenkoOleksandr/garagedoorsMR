from rest_framework import serializers

from employees.models import Employee, Review, SEOEmployee


class EmployeeReviewSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateField(format="%d %b %Y")
    class Meta:
        model = Review
        exclude = ['employee', 'id']


class SEOEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEOEmployee
        exclude = ['employee', 'id']


class EmployeeSerializer(serializers.ModelSerializer):
    seo = SEOEmployeeSerializer()
    reviews = EmployeeReviewSerializer(many=True)
    # photo = serializers.ImageField(source='photo.image')
    state = serializers.CharField(source='state.name')

    class Meta:
        model = Employee
        fields = '__all__'
