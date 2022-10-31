from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Wish(models.Model):
    """ User's wishes model. """

    wish_name = models.CharField(default='', blank=True, null=True, max_length=250)
    user = models.ForeignKey(User, related_name='wishes', on_delete=models.CASCADE)
    announce = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Wish'
        verbose_name_plural = 'Wishes'

    def __str__(self):
        return self.wish_name
