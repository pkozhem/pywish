from django.urls import path
from src.users.views import UserPrivateAPIView, UserPublicAPIView
from src.wall.views import PostListAPIView
from src.wishes.views import WishAPIView
from src.followers.views import FollowerListAPIView


urlpatterns = [
    path('<int:pk>', UserPublicAPIView.as_view({
        'get': 'retrieve'
    })),

    path('<int:pk>/profile', UserPrivateAPIView.as_view({
        'get': 'retrieve',
        'put': 'update'
    })),

    path('<int:pk>/wishes', WishAPIView.as_view({
            'get': 'retrieve',
            'put': 'update'
        })),

    path('<int:pk>/wall', PostListAPIView.as_view()),

    path('<int:pk>/followers', FollowerListAPIView.as_view())
]
