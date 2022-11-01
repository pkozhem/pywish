from django.urls import path
from src.followers.views import FollowerListAPIView, FollowerAPIView

urlpatterns = [
    path('<int:pk>', FollowerAPIView.as_view())
]
