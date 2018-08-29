from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['categories'] = CategorySerializer(
            Category.objects.filter(id__in=data['categories']), many=True).data
        return data
