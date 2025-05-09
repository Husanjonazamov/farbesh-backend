from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import (
    OrderView,
    LocationView
)


router = DefaultRouter()
router.register(r"order", OrderView, basename="order")
router.register("location", LocationView, basename="location")


urlpatterns = [
    path("", include(router.urls)),
]
