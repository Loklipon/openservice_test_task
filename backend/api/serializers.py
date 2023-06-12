from products.models import Price, Product, Type
from rest_framework import serializers


class TypeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения типов товаров.
    """

    class Meta:
        model = Type
        fields = ('__all__')


class PriceSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения цен на товары.
    """
    class Meta:
        model = Price
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения товаров.
    """
    price = PriceSerializer()
    type = TypeSerializer()
    
    class Meta:
        model = Product
        fields = ('__all__')
    
    def create(self, validated_data):
        extract_price = validated_data.pop('price')
        extract_type = validated_data.pop('type')
        if Type.objects.filter(**extract_type).exists():
            type = Type.objects.get(**extract_type)
        else:
            type = Type.objects.create(**extract_type)
        if Price.objects.filter(**extract_price).exists():
            price = Price.objects.get(**extract_price)
        else:
            price = Price.objects.create(**extract_price)
        product = Product.objects.create(price=price, type=type, **validated_data)
        return product
    
    def update(self, instance, validated_data):
        if 'type' in validated_data:
            extract_type = validated_data.pop('type')
            if Type.objects.filter(**extract_type).exists():
                type = Type.objects.get(**extract_type)
            else:
                type = Type.objects.create(**extract_type)
            instance.type = type
            instance.save()
        if 'price' in validated_data:
            extract_price = validated_data.pop('price')
            if Price.objects.filter(**extract_price).exists():
                price = Price.objects.get(**extract_price)
            else:
                price = Price.objects.create(**extract_price)
            instance.price = price
            instance.save()
        return super().update(instance, validated_data)