from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import OrderModel


@register(OrderModel)
class OrderTranslation(TranslationOptions):
    fields = []
