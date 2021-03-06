# Generated by Django 2.2.24 on 2022-05-26 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buoys_app', '0012_auto_20220525_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='agency',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
