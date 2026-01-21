"""Serializers for Test """
from rest_framework.serializers import ModelSerializer
from app.models import TestModel

class TestSerializer(ModelSerializer):
    """test serializer class """
    class Meta:
        "meta options for serializer"
        model = TestModel
        fields = "__all__"

# class UserSerializer(ModelSerializer):
#     """user serializer class """
#     class Meta:
#         "meta options for serializer"
#         model = User
#         fields = "__all__"
