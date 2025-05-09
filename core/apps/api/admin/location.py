from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import LocationModel


@admin.register(LocationModel)
class LocationAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
