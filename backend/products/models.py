from io import BytesIO

import barcode
from barcode.writer import ImageWriter
from django.core.files import File
from django.db import models


class Type(models.Model):
    """
    Тип товаров.
    """
    name = models.CharField(
        max_length=200,
        verbose_name='Название типа',
    )
    description = models.TextField(
        verbose_name='Описание типа товаров'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'тип товара'
        verbose_name_plural = 'Типы товаров'

    def __str__(self):
        return str(self.name)


class Price(models.Model):
    """
    Цена товара.
    """
    value = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Значение'
    )
    currency = models.CharField(
        max_length=3,
        verbose_name='Код валюты'
    )

    class Meta:
        ordering = ('currency', 'value')
        verbose_name = 'цены'
        verbose_name_plural = 'Цены'
        constraints = [
            models.UniqueConstraint(
                fields=('value', 'currency'), name='unique price'
            )
        ]

    def __str__(self):
        return f'{self.value} {self.currency}'


class Product(models.Model):
    """
    Продукт.
    """
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название товара'
    )
    price = models.ForeignKey(
        Price,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Цена товара',
    )
    quantity = models.IntegerField(
        verbose_name='Количество товара, шт.'
    )
    barcode = models.ImageField(
        upload_to='images/',
        blank=True,
        verbose_name='Штрихкод'
    )
    barcode_number = models.CharField(
        max_length=12,
        unique=True,
        verbose_name='Штрихкод'
    )
    date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего изменения'
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.PROTECT,
        verbose_name='Тип товара',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'товары'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.barcode_number}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)
