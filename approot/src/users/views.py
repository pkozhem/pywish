from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet
from src.users.serializers import UserSerializer, UserPublicSerializer
from src.tools.permissions import IsUserOrAdmin

User = get_user_model()


class UserPrivateAPIView(ModelViewSet):
    """ Private User View. """

    permission_classes = [IsAuthenticatedOrReadOnly, IsUserOrAdmin]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


class UserPublicAPIView(ModelViewSet):
    """ Public User View. """

    permission_classes = [AllowAny]
    serializer_class = UserPublicSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])
