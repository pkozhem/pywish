from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from src.users.models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """ Function which creates User's Profile. """

    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    """ Function which saves modified data. """

    instance.profile.save()
