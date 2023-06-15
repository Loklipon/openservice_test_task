from api.views import PriceView, ProductSaleView, ProductView, TypesView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('types', TypesView, basename='types')
router.register('prices', PriceView, basename='prices')
router.register('products', ProductView, basename='products')
urlpatterns = [
    path('products/<int:id>/sale/', ProductSaleView.as_view()),
    path('', include(router.urls)),
]
