# Generated by Django 3.2.9 on 2021-11-27 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0026_appnotifications_id_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='appnotifications',
            name='id_sango',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
