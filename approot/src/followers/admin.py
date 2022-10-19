from django.contrib import admin
from src.followers.models import Follower


class FollowerAdmin(admin.ModelAdmin):
    """ Configuring display list and search fields of Follower model in Admin panel. """

    list_display = ('user', 'follower')
    search_fields = ('user',)


admin.site.register(Follower, FollowerAdmin)
