from django.contrib import admin
from django.utils.html import mark_safe
from products.models import Price, Product, Type


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'price',
                    'quantity', 'date', 'barcode_preview')
    search_fields = ('name',)
    readonly_fields = ('barcode', 'barcode_preview',)

    def barcode_preview(self, obj):
        return mark_safe(f'<img src="{obj.barcode.url}" style="max-height: 65px">')

    barcode_preview.short_description = 'Штрихкод'


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'currency')
