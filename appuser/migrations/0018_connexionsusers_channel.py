# Generated by Django 3.2.5 on 2021-11-08 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0017_usersattachments_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='connexionsusers',
            name='channel',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
