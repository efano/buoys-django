# Generated by Django 2.2.24 on 2022-05-25 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buoys_app', '0010_auto_20220524_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=255),
        ),
    ]