from django.db import models
from django.contrib.auth.models import User

class MailingList(models.Model):
    email = models.EmailField(max_length=100, verbose_name="Пошта для розсилки")
    session_key = models.CharField(max_length=40, verbose_name="Ключ сесії")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")







class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    slug = models.SlugField(unique=True, blank=True,null=True,  verbose_name="Слаг")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    def __str__(self):
        return self.name



class Product(models.Model):
   # rating = models.FloatField(default=0,null=True)
    #number_of_ratings = models.FloatField(default=0)
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="Слаг")
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description=models.CharField(max_length=800, verbose_name="Опис",null=True)
    name = models.CharField(max_length=150, verbose_name="Назва")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категорія")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    session_key = models.CharField(max_length=40, verbose_name="Ключ сесії")
    score = models.IntegerField(verbose_name="Оцінка")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.score} зірок"



class CartItem(models.Model):

    session_key = models.CharField(max_length=40, db_index=True, verbose_name="Ключ сесії",null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Користувач")
    session_key = models.CharField(max_length=40, null=True, blank=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")

    quantity = models.IntegerField(verbose_name="Кількість")

    contact_info = models.CharField(max_length=255, null=True, blank=True,verbose_name="Контакти")
    delivery_method = models.CharField(max_length=100, null=True, blank=True, verbose_name="Спосіб доставки")
    branch_number = models.CharField(max_length=50, null=True, blank=True,verbose_name="Номер відділення")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    def __str__(self):
        return f"Замовлення {self.id} - {self.product.name}"
