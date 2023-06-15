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
        type, created = Type.objects.get_or_create(**extract_type)
        price, created = Price.objects.get_or_create(**extract_price)
        product = Product.objects.create(
            price=price, type=type, **validated_data)
        return product

    def update(self, instance, validated_data):
        if 'type' in validated_data:
            extract_type = validated_data.pop('type')
            type, created = Type.objects.get_or_create(**extract_type)
            instance.type = type
            instance.save()
        if 'price' in validated_data:
            extract_price = validated_data.pop('price')
            price, created = Price.objects.get_or_create(**extract_price)
            instance.price = price
            instance.save()
        return super().update(instance, validated_data)


class ProductSaleSerializer(serializers.ModelSerializer):
    sales = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('sales',)
