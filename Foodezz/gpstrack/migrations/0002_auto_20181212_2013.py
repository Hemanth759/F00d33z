# Generated by Django 2.1.3 on 2018-12-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpstrack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='deliveryid',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, unique=True),
        ),
    ]
