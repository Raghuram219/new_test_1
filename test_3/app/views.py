# """views for test app"""
from rest_framework.viewsets import ModelViewSet
from app.models import TestModel
from app.serializers import TestSerializer

class TestViewSet(ModelViewSet):
    """Viewset for Test Model"""
    # queryset = TestModel.objects.all()
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer


# class UserViewSet(ModelViewSet):
#     """Viewset for Test Model"""
#     # queryset = TestModel.objects.all()
#     queryset = User.objects.all()
#     serializer_class = TestSerializer
#     action_serializers = {
#         "LIST": TestSerializer
#     }

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return TestSerializer
#         return super().get_serializer_class()