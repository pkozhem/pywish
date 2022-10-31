from django.dispatch import receiver
from django.db.models.signals import post_save
from src.wishes.models import Wish
from src.wall.models import Post


@receiver(post_save, sender=Wish)
def create_post_by_wish_update(sender, instance, **kwargs):
    """ Auto create Post when Wish is updated and announce field is True. """

    if instance.announce:
        Post.objects.create(
            text='Just updated wishlist!',
            user=instance.user
        )
