# Generated by Django 4.1.3 on 2023-02-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0039_remove_user_confirmed_at_user_reset_code_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('abonne', 'abonne'), ('census', 'census')], default='abonne', max_length=255, null=True),
        ),
    ]
