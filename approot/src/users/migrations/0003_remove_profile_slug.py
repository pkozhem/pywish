# Generated by Django 4.1.2 on 2022-10-18 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]
