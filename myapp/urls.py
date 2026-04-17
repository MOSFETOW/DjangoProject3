from django.urls import path
from myapp.views import home,products_by_category,product_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('category/<slug:slug>/', products_by_category, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)