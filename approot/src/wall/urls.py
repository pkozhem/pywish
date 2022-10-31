from django.urls import path
from src.wall.views import CommentAPIGenericViewSet, PostAPIGenericViewSet

urlpatterns = [
    path('post/create', PostAPIGenericViewSet.as_view({
        'post': 'create'
    })),

    path('post/<int:pk>', PostAPIGenericViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

    path('comment/create', CommentAPIGenericViewSet.as_view({
        'post': 'create'
    })),

    path('comment/<int:pk>', CommentAPIGenericViewSet.as_view({
        'put': 'update',
        'delete': 'destroy'
    }))
]
