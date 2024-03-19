from rest_framework.serializers import ModelSerializer

from livraria1.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"