from django.urls import path
from myapp.views import home,products_by_category,product_detail,cart,add_to_cart,remove_from_cart,rate_product,search_page,mailing_list,checkout_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cart/checkout', checkout_page,name='checkout_page'),
    path('mailing-list/', mailing_list,name='mailing_list'),
    path('', home,name='home'),
    path('search/', search_page,name='search_page'),

    path('category/<slug:slug>/', products_by_category, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('add-to-cart/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<slug:slug>/', remove_from_cart, name='remove_from_cart'),
    path('rate/<slug:slug>/', rate_product, name='rate_product')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)