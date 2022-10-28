import os
from django.contrib.auth import get_user_model

User = get_user_model()


def delete_previous_image(queryset, current_avatar_path):
    """ Function which deletes previous User's profile image. """

    new_avatar_path = str(queryset.profile.image)
    if current_avatar_path != new_avatar_path and current_avatar_path != 'default.png':
        os.remove('users/media/' + current_avatar_path)
