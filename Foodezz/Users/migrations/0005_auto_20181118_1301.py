# Generated by Django 2.1.3 on 2018-11-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_user_profile_rest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='street',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
