# Generated by Django 3.2.5 on 2021-11-11 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0022_appnotifications_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appnotifications',
            old_name='user',
            new_name='sender',
        ),
    ]
