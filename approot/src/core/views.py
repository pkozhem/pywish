from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)


class CreateRetrieveUpdateDestroyGenericViewSet(GenericViewSet,
                                                CreateModelMixin,
                                                RetrieveModelMixin,
                                                UpdateModelMixin,
                                                DestroyModelMixin):
    """ CRUD Generic View Set base. """

    pass


class CreateUpdateDestroyGenericViewSet(GenericViewSet,
                                        CreateModelMixin,
                                        UpdateModelMixin,
                                        DestroyModelMixin):
    """ CUD Generic View Set base. """

    pass


class RetrieveUpdateGenericViewSet(GenericViewSet,
                                   RetrieveModelMixin,
                                   UpdateModelMixin):
    """ RU Generic View Set base. """

    pass
