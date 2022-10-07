from django.urls import path
from src.users.views import UserPrivateAPIView, UserPublicAPIView

urlpatterns = [
    # path('<slug:slug>/profile', UserView.as_view()),
    # path('<slug:slug>', UserPublicView.as_view()),

    path('<int:pk>', UserPublicAPIView.as_view({'get': 'retrieve'})),
    path('<int:pk>/profile', UserPrivateAPIView.as_view({'get': 'retrieve',
                                                         'put': 'update'}))
]
