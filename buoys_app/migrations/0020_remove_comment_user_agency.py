# Generated by Django 2.2.24 on 2022-05-26 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buoys_app', '0019_auto_20220525_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_agency',
        ),
    ]
