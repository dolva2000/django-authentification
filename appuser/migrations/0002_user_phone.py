# Generated by Django 3.2.5 on 2021-07-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]