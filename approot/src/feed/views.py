from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from src.wall.serializers import PostListSerializer
from src.wall.models import Post


class FeedListAPIView(ListAPIView):
    """ Controller which shows User's feed. """

    permission_classes = [IsAuthenticated]
    serializer_class = PostListSerializer

    def list(self, request, *args, **kwargs):
        queryset = Post.objects.filter(user__owner__follower=request.user).order_by('-date_updated')\
            .select_related('user').prefetch_related('comments')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
