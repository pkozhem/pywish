# Generated by Django 4.1 on 2022-09-20 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wall', '0005_remove_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, default='', max_length=512, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('published_cond', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='wall.commentpost')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='wall.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post Comment',
                'verbose_name_plural': 'Post Comments',
            },
        ),
    ]
