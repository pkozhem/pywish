# Generated by Django 4.1 on 2022-09-20 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0004_rename_date_post_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]