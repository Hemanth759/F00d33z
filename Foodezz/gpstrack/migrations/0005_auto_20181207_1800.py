# Generated by Django 2.1.3 on 2018-12-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpstrack', '0004_auto_20181115_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='currlocation',
        ),
        migrations.AddField(
            model_name='driver',
            name='lat',
            field=models.FloatField(default=522333555, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='long',
            field=models.FloatField(default=5.1155215, max_length=30),
            preserve_default=False,
        ),
    ]
