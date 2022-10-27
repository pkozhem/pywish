from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    """ Default User model inherited from Django's Abstract User model. """

    pass

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Profile(models.Model):
    """ User's Profile model. Creates automatically when new user is created. """

    SEX = (('male', 'male'),
           ('female', 'female'))
    birthday = models.DateField(blank=True, null=True)
    sex = models.CharField(default='male', max_length=6, choices=SEX)
    image = models.ImageField(default='default.png', upload_to='avatars', blank=True, null=True)
    status = models.CharField(default='All is good!', blank=True, null=True, max_length=255)
    bio = models.CharField(default='', blank=True, null=True, max_length=255)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def save(self, *args, **kwargs):
        """ Overwritten save method that resizes image. """

        super().save(*args, **kwargs)
        resized_image = Image.open(self.image.path)
        if resized_image.height > 300 or resized_image.width > 300:
            resized_image.thumbnail((300, 300))
            resized_image.save(self.image.path)

    def __str__(self):
        return self.user
