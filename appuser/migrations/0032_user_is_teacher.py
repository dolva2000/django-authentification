# Generated by Django 3.2.9 on 2022-05-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0031_smssend'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
