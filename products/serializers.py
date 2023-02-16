from rest_framework import serializers
from products.models import ProductMain, ProductImage


class ProductMainModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductMain
        fields = '__all__'


class ProductImageModelSerializer(serializers.ModelSerializer):
    product = ProductMainModelSerializer()

    class Meta:
        model = ProductImage
        fields = '__all__'
