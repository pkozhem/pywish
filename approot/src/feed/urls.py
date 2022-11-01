from django.urls import path
from src.feed.views import FeedListAPIView

urlpatterns = [
    path('', FeedListAPIView.as_view())
]
