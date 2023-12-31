# Generated by Django 3.2.7 on 2021-09-10 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0005_auto_20210723_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnexionsUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_connexions_users',
            },
        ),
        migrations.CreateModel(
            name='UsersAttachments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(max_length=255, upload_to='photos/%Y/%m/%d/')),
                ('temp_path', models.TextField(blank=True, null=True)),
                ('is_done', models.BooleanField(default=False, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('size', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=60, null=True)),
                ('expired_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_users_attachments',
            },
        ),
        migrations.DeleteModel(
            name='Attachments',
        ),
    ]
