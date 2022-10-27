from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from src.wishes.models import Wish
from src.wishes.serializers import WishSerializer
from src.tools.views import RetrieveUpdateGenericViewSet
from src.tools.permissions import IsOwnerOrAdmin

User = get_user_model()


class WishAPIView(RetrieveUpdateGenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = WishSerializer

    def get_queryset(self):
        user = User.objects.get(id=self.kwargs['pk'])
        return Wish.objects.filter(user=user)

    def get_permissions(self):
        if self.action == 'get':
            self.permission_classes = [AllowAny]
        elif self.action == 'update':
            self.permission_classes = [IsOwnerOrAdmin]
        return super(self.__class__, self).get_permissions()
