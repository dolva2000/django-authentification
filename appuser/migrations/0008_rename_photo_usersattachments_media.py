# Generated by Django 3.2.7 on 2021-09-16 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0007_alter_usersattachments_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersattachments',
            old_name='photo',
            new_name='media',
        ),
    ]
