from django.urls import path
from src.wall.views import PostListAPIView, CommentAPIView, PostAPIView

urlpatterns = [
    path('<slug:slug>', PostListAPIView.as_view()),  # wall/user-slug  'user's wall'
    path('post/create', PostAPIView.as_view({'post': 'create'})),  # wall/post/create  'create post'
    path('post/<int:pk>', PostAPIView.as_view({'get': 'retrieve',  # wall/post/id  'actions with post'
                                               'put': 'update',
                                               'delete': 'destroy'})),
    path('comment/create', CommentAPIView.as_view({'post': 'create'})),  # wall/comment/create  'create comment'
    path('comment/<int:pk>', CommentAPIView.as_view({'put': 'update',    # wall/comment/id  'actions with comment'
                                                     'delete': 'destroy'}))
]
