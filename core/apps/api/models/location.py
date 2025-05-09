from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class LocationModel(AbstractBaseModel):
    name = models.CharField(
        verbose_name=_("Nomi"), 
        max_length=255,
        blank=True,
        null=True
    )
    lat = models.FloatField(
        verbose_name=_("Kenglik"),
        default=0,
        blank=True,
        null=True
    )
    long = models.FloatField(
        verbose_name=_("Uzunlik"),
        default=0,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name if self.name else "No Name"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "location"
        verbose_name = _("LocationModel")
        verbose_name_plural = _("LocationModels")
