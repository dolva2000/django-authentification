# Generated by Django 3.2.5 on 2021-11-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0023_rename_user_appnotifications_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='connexionsusers',
            name='device',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='connexionsusers',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]