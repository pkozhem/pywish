# Generated by Django 4.1 on 2022-09-15 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]