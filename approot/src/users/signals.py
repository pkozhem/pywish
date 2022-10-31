from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from src.users.models import Profile
from src.wishes.models import Wish

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile_and_wish(sender, instance, created, **kwargs):
    """ Auto create Profile and Wish when User is created. """

    if created:
        Profile.objects.create(user=instance)
        Wish.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_profile_and_wish(sender, instance, **kwargs):
    """ Saves incoming data for Profile instantly . """

    instance.profile.save()
