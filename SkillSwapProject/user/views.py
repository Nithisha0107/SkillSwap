from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import Userserializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer

    def perform_create(self, serializer):
        import pdb;pdb.set_trace()
        User.objects.create_user(**serializer.data)