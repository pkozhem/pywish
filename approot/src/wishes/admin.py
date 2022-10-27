from django.contrib import admin
from src.wishes.models import Wish


class WishAdmin(admin.ModelAdmin):
    """ Configuring display list and search fields of Wish model in Admin panel. """

    list_display = ('wish_name', 'user')
    search_fields = ('wish_name', 'user')


admin.site.register(Wish, WishAdmin)
