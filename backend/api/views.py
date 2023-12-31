from http import HTTPStatus

from api.serializers import (PriceSerializer, ProductSaleSerializer,
                             ProductSerializer, TypeSerializer)
from django.shortcuts import get_object_or_404
from products.models import Price, Product, Type
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class TypesView(viewsets.ModelViewSet):
    """
    Вью-сет для добавления, обновления,
    чтения, и удаления типов товаров.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class PriceView(viewsets.ModelViewSet):
    """
    Вью-сет для добавления, обновления,
    чтения, и удаления цен товаров.
    """
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class ProductView(viewsets.ModelViewSet):
    """
    Вью-сет для добавления, обновления,
    чтения, и удаления товаров.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductSaleView(APIView):
    """
    Вью-класс для уменьшения
    остатка товара.
    """
    def post(self, request, id):
        serializer = ProductSaleSerializer(data=request.data)
        if serializer.is_valid():
            sale = serializer.data.get('sales')
            product = get_object_or_404(Product, pk=id)
            product.quantity = product.quantity - sale
            product.save()
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=HTTPStatus.OK)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)