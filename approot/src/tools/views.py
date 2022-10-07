from rest_framework import mixins, viewsets


class PermissionsMixinViewSet(viewsets.ViewSet):
    """ Permission Mixin plus ViewSet. """

    pass


class PermissionsMixinGenericViewSet(viewsets.GenericViewSet):
    """ Permission Mixin plus GenericViewSet. """

    pass


class CreateUpdateDestroyView(viewsets.GenericViewSet,
                              mixins.CreateModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin):
    """ CUD Mixin. """

    pass


class CreateRetrieveUpdateDestroyView(viewsets.GenericViewSet,
                                      mixins.CreateModelMixin,
                                      mixins.RetrieveModelMixin,
                                      mixins.UpdateModelMixin,
                                      mixins.DestroyModelMixin):
    """ CRUD Mixin. """

    pass
