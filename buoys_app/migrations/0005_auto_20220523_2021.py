# Generated by Django 2.2.24 on 2022-05-24 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buoys_app', '0004_auto_20220523_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_name',
            new_name='user_post',
        ),
    ]
