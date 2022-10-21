from django.db import models
from django.contrib.auth import get_user_model
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

User = get_user_model()


class Post(models.Model):
    """ Post model. """

    text = models.TextField(default='', blank=True, null=True, max_length=1024)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    published_cond = models.BooleanField(default=True)
    views_amount = models.PositiveIntegerField(default=0, null=False)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def comments_amount(self):
        return self.comments.count()

    def __str__(self):
        return f'{self.text}'


class Comment(MPTTModel, models.Model):
    """ Comment on Post model with possibility reply to any comment. """

    text = models.TextField(default='', blank=True, null=True, max_length=512)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    published_cond = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return '{} by {}'.format(self.post, self.user)
