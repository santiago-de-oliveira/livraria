from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from livraria1.models import Categoria
from livraria1.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


