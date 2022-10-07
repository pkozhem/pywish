from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from src.wall.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    """ Configuring display list and search fields of Post model in Admin panel. """

    list_display = ('text', 'user', 'date_created', 'published_cond', 'views_amount')
    search_fields = ('text', 'user', 'date_created', 'published_cond')


class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """ Configuring display list and search fields of Comment on Post model in Admin panel. """

    list_display = ('text', 'post', 'parent', 'user', 'date_created', 'published_cond')
    search_fields = ('text', 'post', 'parent', 'user', 'date_created', 'published_cond')
    mptt_level_indent = 15


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
