from rest_framework import serializers

from services.models import Service, ServiceCategory, ServiceReview, SEOServiceArticle, ServiceArticle


class SEOServiceArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEOServiceArticle


class ServiceReviewSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d %b %Y")

    class Meta:
        model = ServiceReview
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceArticleSerializer(serializers.ModelSerializer):
    seo = SEOServiceArticleSerializer()

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
    image = serializers.ImageField(source='image.image')
    category = serializers.CharField(source='category.name')
