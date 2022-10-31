from django.apps import AppConfig


class WallConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.wall'

    def ready(self):
        """ Activating signals. """

        from src.wall import signals
