# Generated by Django 4.1.2 on 2022-10-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='wish_name',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]
