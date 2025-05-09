from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import OrderModel


@admin.register(OrderModel)
class OrderAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
