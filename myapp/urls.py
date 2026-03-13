from django.urls import path
from myapp.views import home, page1, page2

urlpatterns = [
    path('', home),
    path('page1/', page1),
    path('page2/', page2),
]