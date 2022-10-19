from django.urls import path
from src.followers.views import FollowerListAPIView, FollowerAPIView

urlpatterns = [
    path('<int:pk>/follow', FollowerAPIView.as_view()),
    path('<int:pk>', FollowerListAPIView.as_view())
]
