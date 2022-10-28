from rest_framework import serializers


class CommentParentListSerializer(serializers.ListSerializer):
    """ Parent comments serializer (without children). """

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveChildrenSerializer(serializers.Serializer):
    """ Recursive children serializer. """

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
