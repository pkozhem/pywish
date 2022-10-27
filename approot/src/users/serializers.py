from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from src.users.models import Profile
from src.wishes.serializers import WishSerializer

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    """ User's Profile model serializer. """

    class Meta:
        model = Profile
        fields = (
            'id',
            'birthday',
            'sex',
            'image',
            'status',
            'bio'
        )


class ProfileImageSerializer(serializers.ModelSerializer):
    """ Profile image serializer. """

    class Meta:
        model = Profile
        fields = (
            'image'
        )


class UserPrivateSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    """ User serializer. """

    profile = ProfileSerializer(many=False, required=False)
    wishes = WishSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = User
        exclude = (
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser"
        )


class UserPublicSerializer(serializers.ModelSerializer):
    """ Public User serializer. """

    profile = ProfileSerializer(many=False, required=False)
    wishes = WishSerializer(many=True, required=False)

    class Meta:
        model = User
        exclude = (
            "password",
            "email",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser"
        )
