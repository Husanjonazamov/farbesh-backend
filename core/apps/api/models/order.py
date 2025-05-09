from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class GenderChoice(models.TextChoices):
    MALE = "male", "Erkak",
    FEMALE = "female", "Ayol"
    OTHER = "other", "Pochta"
    
    
class PeopleCountChoices(models.TextChoices):
    ONE = "one", "1 kishi"
    TWO = "two", "2 kishi"
    THERE = "there", "3 kishi"
    FOUR = "four", "4 kishi"


class OrderModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("Ism"), max_length=255)
    phone = models.CharField(
        verbose_name=_("Telefon raqam"),
        max_length=100,
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        "api.LocationModel",
        verbose_name=_("Manzil"),
        on_delete=models.CASCADE,
        related_name="order"
    )
    gender = models.CharField(
        verbose_name=_("Jins"),
        max_length=100,
        choices=GenderChoice.choices,
        default=GenderChoice.MALE,
    )
    count = models.CharField(
        verbose_name=_("Odam soni"),
        max_length=100,
        choices=PeopleCountChoices.choices,
        default=PeopleCountChoices.ONE
    )

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "order"
        verbose_name = _("OrderModel")
        verbose_name_plural = _("OrderModels")
