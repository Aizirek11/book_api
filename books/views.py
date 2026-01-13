from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Books
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

# Create your views here.
