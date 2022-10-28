from rest_framework import permissions, generics
from src.core.permissions import IsOwnerOrAdmin
from src.core.views import CreateRetrieveUpdateDestroyGenericViewSet, CreateUpdateDestroyGenericViewSet
from src.wall.models import Post, Comment
from src.wall.serializers import CommentCreateSerializer, PostSerializer, PostListSerializer


class PostAPIGenericViewSet(CreateRetrieveUpdateDestroyGenericViewSet):
    """ Post's CRUD. """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().select_related('user').prefetch_related('comments')

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

    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(user__id=self.kwargs['pk']).select_related('user').prefetch_related('comments')


class CommentAPIGenericViewSet(CreateUpdateDestroyGenericViewSet):
    """ Comment's CUD. """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            self.permission_classes = [IsOwnerOrAdmin]
        return super(self.__class__, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def perform_destroy(self, instance):
    #     instance.published_cond = False
    #     instance.save()
