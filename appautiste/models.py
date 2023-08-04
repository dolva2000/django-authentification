from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from appuser.models import User

# Create your models here.

class autiste (models.Model):
    prenom = models.CharField(max_length=255, blank=True, null=True)
    postnom = models.CharField(max_length=255, blank=True, null=True)
    nom = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=20, blank=True, null=True)
    compte_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        db_table="tb_autiste"
