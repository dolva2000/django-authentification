# Generated by Django 3.2.9 on 2022-08-14 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0033_user_sexe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='sexe',
            new_name='genre',
        ),
    ]
