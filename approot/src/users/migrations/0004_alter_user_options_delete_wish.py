# Generated by Django 4.1.2 on 2022-10-27 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.DeleteModel(
            name='Wish',
        ),
    ]
