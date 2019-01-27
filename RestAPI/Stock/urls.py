from django.urls import path
from .views import ProductsView, ProductsAPIView

urlpatterns = [
    path('', ProductsAPIView.as_view(), name='Products'),
    path('', ProductsView.as_view(), name='Single Product')
]