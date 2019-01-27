from rest_framework import generics
from .models import Products
from .serializers import ProductSerializers


class ProductsAPIView(generics.ListAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        return Products.objects.all()


class ProductsView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ProductSerializers

    def get_queryset(self):
        return Products.objects.all()
