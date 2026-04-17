
from django.shortcuts import render
from .models import Product,Category
from django.shortcuts import render,get_object_or_404

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        "title": "Головна сторінка",
        "content": "Це головна сторінка сайту",
        "is_home": True,
        'products': products,
        'categories': categories,
    }
    return render(request, "page.html", context)


def products_by_category(request, slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'categories.html', context)



def product_detail(request, category_slug, product_slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, slug=product_slug, category=category)
    products = Product.objects.filter(category=category)
    context={
        'product': product,
        'category': category,
        'products': products,
        'categories': categories
    }
    return render(request, 'product_detail.html', context)



