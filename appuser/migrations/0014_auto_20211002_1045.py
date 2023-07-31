# Generated by Django 3.2.7 on 2021-10-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0013_auto_20211002_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, default='Congo, the Democratic Republic of the', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='iso3Code',
            field=models.CharField(blank=True, default='COD', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='isoCode',
            field=models.CharField(blank=True, default='CD', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneCode',
            field=models.CharField(blank=True, default='243', max_length=10, null=True),
        ),
    ]
