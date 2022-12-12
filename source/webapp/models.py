from django.db import models
from django.core.validators import MinValueValidator

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = ((DEFAULT_CATEGORY, 'разное'), ('food', 'еда'), ('drinks', 'напитки'), ('sweets', 'сладости'),)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание товара')
    category = models.CharField(max_length=30, default=DEFAULT_CATEGORY, choices=CATEGORY_CHOICES,
                                verbose_name='Категория товара')
    amount = models.PositiveIntegerField(verbose_name='Остаток товара')
    price = models.DecimalField(verbose_name='Цена товара', max_digits=7, decimal_places=2,
                                validators=(MinValueValidator(0),))

    def __str__(self):
        return f'{self.name} - {self.amount}'
