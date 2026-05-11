
from django.db.models import Q
from django.shortcuts import render,redirect
from .models import Product,Category,CartItem,Rating,MailingList,Order
from django.shortcuts import render,get_object_or_404


def checkout_page(request):
    if request.method == 'POST':
        if not request.session.session_key:
            request.session.create()
        s_key = request.session.session_key

        selected_ids = request.POST.getlist('selected_id')
        item_ids = request.POST.getlist('item_id')
        quantities = request.POST.getlist('quantity')


        contact_info = request.POST.get('contact_info')
        delivery_method = request.POST.get('delivery_method')
        branch_number = request.POST.get('branch_number')

        for i in range(len(item_ids)):
            item_id = item_ids[i]
            quantity = quantities[i]

            cart_map = dict(zip(item_ids, quantities))


        for c_id, q_val in cart_map.items():
            CartItem.objects.filter(id=c_id, session_key=s_key).update(quantity=q_val)

        items_to_order = CartItem.objects.filter(id__in=selected_ids, session_key=s_key)


        if items_to_order.exists():
            for item in items_to_order:

                Order.objects.create(
                    session_key=s_key,
                    product=item.product,
                    quantity=item.quantity,
                    contact_info=contact_info,
                    delivery_method=delivery_method,
                    branch_number=branch_number
                )


            items_to_order.delete()

            return redirect("home")

    return redirect("cart")





def mailing_list(request):
    email = request.POST.get('e')

    if email:
        #product = get_object_or_404(Product, slug=slug)
        s_key = get_session_key(request)


        existing_email = MailingList.objects.filter(session_key=s_key).first()

        if existing_email:

            existing_email.email = email
            existing_email.save()
        else:

            MailingList.objects.create(session_key=s_key, email=email)


    return redirect("home")



def search_page(request):
    query = request.POST.get('q').lower()
#
    results= {}
    if query:

        results = Product.objects.filter(
            Q(name__iregex=query) | Q(description__iregex=query)
        )

        if len(results) == 0 :
            results = Product.objects.all()

    print(results)

    categories = Category.objects.all()
    context = {
        'products': results,
        'categories': categories,
        "search_tool":True
    }
    return render(request, "page.html", context)



def product_detail(request, category_slug, product_slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, slug=product_slug, category=category)
    products = Product.objects.filter(category=category)  # Для схожих товарів


    print(Rating.objects.all())
    print(categories)
    all_ratings = Rating.objects.filter(product=product)
    ratings_count = all_ratings.count()


    average_rating = 0
    if ratings_count > 0:
        total_score = sum(rating.score for rating in all_ratings)
        average_rating = round(total_score / ratings_count, 1)


    s_key = get_session_key(request)
    user_rating_obj = Rating.objects.filter(product=product, session_key=s_key).first()

    user_score = 0
    if user_rating_obj:
        user_score = user_rating_obj.score


    context = {
        'product': product,
        'category': category,
        'products': products,
        'categories': categories,
        'average_rating': average_rating,
        'ratings_count': ratings_count,
        'user_score': user_score,
    }
    return render(request, 'product_detail.html', context)



def rate_product(request, slug):
    if request.method == 'POST':
        score = request.POST.get('score')


        if score and score.isdigit() and 1 <= int(score) <= 5:
            product = get_object_or_404(Product, slug=slug)
            s_key = get_session_key(request)


            existing_rating = Rating.objects.filter(product=product, session_key=s_key).first()

            if existing_rating:

                existing_rating.score = int(score)
                existing_rating.save()
            else:

                Rating.objects.create(product=product, session_key=s_key, score=int(score))


    product = get_object_or_404(Product, slug=slug)
    return redirect('product_detail', category_slug=product.category.slug, product_slug=slug)



def get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def add_to_cart(request,slug):
    product = get_object_or_404(Product, slug=slug)
    s_key = get_session_key(request)

    cart_item, created = CartItem.objects.get_or_create(
        session_key=s_key,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def remove_from_cart(request, slug):

    s_key = get_session_key(request)

    cart_item = get_object_or_404(CartItem, id=slug, session_key=s_key)
    cart_item.delete()
    return redirect('cart')


def cart(request):
    s_key = get_session_key(request)
    items = CartItem.objects.filter(session_key=s_key)
    categories = Category.objects.all()

    return render(request, 'cart.html', {
        'items': items,
        'categories': categories,
    })


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











#def product_detail(request, category_slug, product_slug):
    #   categories = Category.objects.all()
    #  category = get_object_or_404(Category, slug=category_slug)
    #  product = get_object_or_404(Product, slug=product_slug, category=category)
    #  products = Product.objects.filter(category=category)
    #   context={
    #      'product': product,
    #      'category': category,
    #     'products': products,
    #     'categories': categories
    # }
# return render(request, 'product_detail.html', context)
#