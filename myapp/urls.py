from django.urls import path
from myapp.views import home, page1, page2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('page1/', page1),
    path('page2/', page2),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)