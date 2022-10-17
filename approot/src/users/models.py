from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from PIL import Image


class User(AbstractUser):
    """ Default User model inherited from Django's Abstract User model. """

    pass

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'UserView'

    def __str__(self):
        return f'{self.username}'


class Profile(models.Model):
    """ User's Profile model. Creates automatically when new user is created. """

    SEX = (('male', 'male'),
           ('female', 'female'))
    slug = models.SlugField(default='', blank=True, unique=True)
    birthday = models.DateField(blank=True, null=True)
    sex = models.CharField(default='male', max_length=6, choices=SEX)
    image = models.ImageField(default='default.png', upload_to='avatars', blank=True, null=True)
    status = models.CharField(default='All is good!', blank=True, null=True, max_length=255)
    bio = models.CharField(default='', blank=True, null=True, max_length=255)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """ Overwritten save method. Makes slug and resizes image. """

        self.slug = slugify(self.user)
        super().save(*args, **kwargs)
        resized_image = Image.open(self.image.path)
        if resized_image.height > 300 or resized_image.width > 300:
            resized_image.thumbnail((300, 300))
            resized_image.save(self.image.path)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.user}'


class Wish(models.Model):
    """ User's wishes model. """

    wish_name = models.CharField(blank=True, null=True, max_length=250)
    user = models.ForeignKey(User, related_name='wishes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Wish'
        verbose_name_plural = 'Wishes'

    def __str__(self):
        return f'{self.wish_name} by {self.user}'
