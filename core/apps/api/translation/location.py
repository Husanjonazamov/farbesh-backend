from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import LocationModel


@register(LocationModel)
class LocationTranslation(TranslationOptions):
    fields = []
