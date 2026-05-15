from django.urls import path, include
from myapp.views import home, products_by_category, product_detail, cart, add_to_cart, remove_from_cart, rate_product, \
    search_page, mailing_list, checkout_page, register_view, profile_view,password_update_send_code,password_update_verify,password_update_final, custom_logout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('profile/update-password/send/', password_update_send_code, name='password_update_send_code'),
    path('profile/update-password/verify/', password_update_verify, name='password_update_verify'),
    path('profile/update-password/confirm/', password_update_final, name='password_update_final'),
    path('logout/', custom_logout, name='logout'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),


    path('cart/checkout', checkout_page,name='checkout_page'),
    path('mailing-list/', mailing_list, name='mailing_list'),
    path('', home, name='home'),
    path('search/', search_page, name='search_page'),
    path('category/<slug:slug>/', products_by_category, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('add-to-cart/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<slug:slug>/', remove_from_cart, name='remove_from_cart'),
    path('rate/<slug:slug>/', rate_product, name='rate_product')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)