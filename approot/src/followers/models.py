from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Follower(models.Model):
    """ Follower model. Field 'follower' - who subscribing. Field 'user' - subscribed to it. """

    follower = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Follower'
        verbose_name_plural = 'Followers'

    def __str__(self):
        return self.follower
