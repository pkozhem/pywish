from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.users'

    def ready(self):
        """ Activating signals. """

        from src.users import signals
