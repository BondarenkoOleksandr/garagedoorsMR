from rest_framework import serializers

from services.models import Service, ServiceCategory, ServiceReview, ServiceArticle, SEOService


class SEOServiceArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEOService
        fields = '__all__'


class ServiceReviewSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d %b %Y")
    state = serializers.CharField(source='city.state.name')

    class Meta:
        model = ServiceReview
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='image.image', allow_null=True)
    image__alt = serializers.CharField(source='image.alt', allow_null=True)
    image__title = serializers.CharField(source='image.title', allow_null=True)
    seo = SEOServiceArticleSerializer()

    class Meta:
        model = Service
        fields = '__all__'


class ServiceArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceArticle
        exclude = ['article']


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'


class ServiceDetailSerializer(ServiceSerializer):
    reviews = ServiceReviewSerializer(many=True)
    article = ServiceArticleSerializer()
    image = serializers.ImageField(source='image.image', allow_null=True)
    image__alt = serializers.CharField(source='image.alt', allow_null=True)
    image__title = serializers.CharField(source='image.title', allow_null=True)
    category = serializers.CharField(source='category.name')
