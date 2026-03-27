from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")




class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категорія")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")




class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.IntegerField(verbose_name="Кількість")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")


