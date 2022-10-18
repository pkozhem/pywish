from django.contrib.auth import get_user_model
from rest_framework import serializers
from src.followers.models import Follower
from src.tools.serializers import ProfileImageSerializer

User = get_user_model()


class UserFollowerSerializer(serializers.ModelSerializer):
    """ Serializer for follower field in FollowerSerializer. """

    profile = ProfileImageSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )


class FollowerSerializer(serializers.ModelSerializer):
    """ Follower serializer. """

    follower = UserFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = (
            'follower',
        )
