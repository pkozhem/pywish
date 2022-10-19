from django.urls import path
from src.wall.views import PostListAPIView, CommentAPIGenericViewSet, PostAPIGenericViewSet

urlpatterns = [
    path('<int:pk>', PostListAPIView.as_view()),                             # wall/user-id  'user's wall'
    path('post/create', PostAPIGenericViewSet.as_view({'post': 'create'})),  # wall/post/create  'create post'
    path('post/<int:pk>', PostAPIGenericViewSet.as_view({'get': 'retrieve',  # wall/post/post-id  'actions with post'
                                                         'put': 'update',
                                                         'delete': 'destroy'})),
    path('comment/create', CommentAPIGenericViewSet.as_view({'post': 'create'})),  # wall/comment/create  'create'
    path('comment/<int:pk>', CommentAPIGenericViewSet.as_view({'put': 'update',    # wall/comment/comment-id  'actions'
                                                               'delete': 'destroy'}))
]
