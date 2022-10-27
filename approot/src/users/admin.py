from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from src.users.models import Profile

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    """ Configuring display list and search fields of Profile model in Admin panel. """

    list_display = ('user', 'image', 'status')
    search_fields = ('user',)


admin.site.register(Profile, ProfileAdmin)
