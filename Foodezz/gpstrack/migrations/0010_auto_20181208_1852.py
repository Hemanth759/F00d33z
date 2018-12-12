# Generated by Django 2.1.3 on 2018-12-08 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpstrack', '0009_auto_20181208_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='deliveryid',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='driver',
            name='restid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.RestaurantLog'),
        ),
    ]