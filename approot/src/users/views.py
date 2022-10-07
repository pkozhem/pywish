from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from src.users.serializers import UserSerializer, UserPublicSerializer
from src.tools.permissions import IsUserOrAdmin

User = get_user_model()


class UserPrivateAPIView(viewsets.ModelViewSet):
    """ Private User View. """

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk']).all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrAdmin]
    queryset = get_queryset
    serializer_class = UserSerializer


class UserPublicAPIView(viewsets.ModelViewSet):
    """ Public User View. """

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk']).all()

    permission_classes = [permissions.AllowAny]
    queryset = get_queryset
    serializer_class = UserPublicSerializer
