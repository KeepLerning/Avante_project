from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import CostumUser

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        CostumUser.objects.create(id_user=instance, Nomor_phone=instance.n_phone)