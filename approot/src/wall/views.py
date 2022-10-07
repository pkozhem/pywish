from rest_framework import permissions, generics
from src.tools.permissions import IsOwnerOrAdmin
from src.tools.views import CreateRetrieveUpdateDestroyView, CreateUpdateDestroyView
from src.wall.models import Post, Comment
from src.wall.serializers import CommentCreateSerializer, PostSerializer, PostListSerializer


class PostAPIView(CreateRetrieveUpdateDestroyView):
    """ Post's CRUD. """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().select_related('user').prefetch_related('comments')
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            self.permission_classes = [IsOwnerOrAdmin]
        elif self.action == 'get':
            self.permission_classes = [permissions.AllowAny]
        return super(self.__class__, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostListAPIView(generics.ListAPIView):
    """ List of Posts in User's wall. """

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(user__profile__slug=slug).select_related('user').prefetch_related('comments')

    serializer_class = PostListSerializer


class CommentAPIView(CreateUpdateDestroyView):
    """ Comment's CUD. """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            self.permission_classes = [IsOwnerOrAdmin]
        return super(self.__class__, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.published_cond = False
        instance.save()
