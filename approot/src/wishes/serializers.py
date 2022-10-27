from django.contrib.auth import get_user_model
from rest_framework import serializers
from src.wishes.models import Wish

User = get_user_model()


class WishSerializer(serializers.ModelSerializer):
    """ Wish model serializer. """

    class Meta:
        model = Wish
        fields = (
            'id',
            'wish_name'
        )
