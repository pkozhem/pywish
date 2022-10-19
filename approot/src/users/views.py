from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet
from src.users.serializers import UserSerializer, UserPublicSerializer
from src.tools.permissions import IsUserOrAdmin

User = get_user_model()


class UserPrivateAPIView(ModelViewSet):
    """ Private User View. """

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk']).all()

    permission_classes = [IsAuthenticatedOrReadOnly, IsUserOrAdmin]
    queryset = get_queryset
    serializer_class = UserSerializer


class UserPublicAPIView(ModelViewSet):
    """ Public User View. """

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk']).all()

    permission_classes = [AllowAny]
    queryset = get_queryset
    serializer_class = UserPublicSerializer
