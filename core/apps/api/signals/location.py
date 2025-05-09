from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import LocationModel


@receiver(post_save, sender=LocationModel)
def LocationSignal(sender, instance, created, **kwargs): ...
