from api.views import PriceView, ProductSaleView, ProductView, TypesView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('types', TypesView, basename='types')
router.register('prices', PriceView, basename='pices')
router.register('products', ProductView, basename='pices')
urlpatterns = [
    path('', include(router.urls)),
    path('sale/<int:pk>/<int:amount>', ProductSaleView.as_view())
]
