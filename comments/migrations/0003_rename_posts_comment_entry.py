# Generated by Django 5.1 on 2024-08-29 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_rename_post_comment_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='posts',
            new_name='entry',
        ),
    ]
