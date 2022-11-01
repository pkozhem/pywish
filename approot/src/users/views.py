from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet
from src.users.serializers import UserPrivateSerializer, UserPublicSerializer
from src.core.permissions import IsUserOrAdmin

User = get_user_model()


class UserPrivateAPIView(ModelViewSet):
    """ Private User Controller. """

    permission_classes = [IsAuthenticatedOrReadOnly, IsUserOrAdmin]
    serializer_class = UserPrivateSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk']).select_related('profile').prefetch_related('wishes')


class UserPublicAPIView(ModelViewSet):
    """ Public User Controller. """

    permission_classes = [AllowAny]
    serializer_class = UserPublicSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk']).select_related('profile').prefetch_related('wishes')
