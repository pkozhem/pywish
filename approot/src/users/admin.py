from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from src.users.models import Profile, Wish

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    """ Configuring display list and search fields of Profile model in Admin panel. """

    list_display = ('user', 'slug', 'image', 'status')
    search_fields = ('user', 'slug')


class WishAdmin(admin.ModelAdmin):
    """ Configuring display list and search fields of Wish model in Admin panel. """

    list_display = ('wish_name', 'user')
    search_fields = ('wish_name', 'user')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Wish, WishAdmin)
