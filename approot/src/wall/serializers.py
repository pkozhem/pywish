from rest_framework import serializers
from src.wall.models import Post, Comment
from src.tools.serializers import RecursiveChildrenSerializer, CommentParentListSerializer


class CommentCreateSerializer(serializers.ModelSerializer):
    """ Create Comment serializer. """

    class Meta:
        model = Comment
        fields = (
            'post',
            'text',
            'parent'
        )


class CommentListSerializer(serializers.ModelSerializer):
    """ List of Comments serializer. """

    user = serializers.ReadOnlyField(source='user.username')
    children = RecursiveChildrenSerializer(many=True)

    @staticmethod
    def get_text(obj):
        if obj.published_cond:
            return obj.text
        return None

    class Meta:
        model = Comment
        list_serializer_class = CommentParentListSerializer
        fields = (
            'id',
            'post',
            'user',
            'text',
            'date_created',
            'date_updated',
            'published_cond',
            'children'
        )


class PostSerializer(serializers.ModelSerializer):
    """ Single Post serializer for CRUD. """

    user = serializers.ReadOnlyField(source='user.username')
    comments = CommentListSerializer(many=True, read_only=True)
    views_amount = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'text',
            'date_created',
            'date_updated',
            'views_amount',
            'comments'
        )


class PostListSerializer(serializers.ModelSerializer):
    """ List of Posts serializer. """

    user = serializers.ReadOnlyField(source='user.username')
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'text',
            'date_created',
            'date_updated',
            'views_amount',
            'comments_amount',
            'published_cond',
            'comments'
        )
