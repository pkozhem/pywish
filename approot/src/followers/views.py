from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from src.followers.models import Follower
from src.followers.serializers import FollowerSerializer

User = get_user_model()


class FollowerListAPIView(ListAPIView):
    """ View allows to show User's followers. """

    def get_queryset(self):
        return Follower.objects.filter(user=self.kwargs['pk']).all()

    permission_classes = [AllowAny]
    queryset = get_queryset
    serializer_class = FollowerSerializer


class FollowerAPIView(APIView):
    """ Create and destroy Follower (follow and unfollow) API View. """
    # REMINDER NOTE: Delete attr data later

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user = User.objects.get(id=self.kwargs['pk'])

        if User.objects.filter(followers__user=user, followers__follower=request.user):
            return Response(data={"details": "You are already following this user."},
                            status=status.HTTP_204_NO_CONTENT)

        Follower.objects.create(user=user, follower=request.user)
        return Response(data={"details": f"{request.user} started follow {user}."},
                        status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        user = User.objects.get(id=self.kwargs['pk'])
        Follower.objects.get(user=user, follower=request.user).delete()
        return Response(data={"details": f"{request.user} no more follows {user}."},
                        status=status.HTTP_204_NO_CONTENT)
