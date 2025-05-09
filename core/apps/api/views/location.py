from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import LocationModel
from core.apps.api.serializers.location import (
    CreateLocationSerializer,
    ListLocationSerializer,
    RetrieveLocationSerializer,
)


@extend_schema(tags=["location"])
class LocationView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = LocationModel.objects.all()
    serializer_class = ListLocationSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListLocationSerializer,
        "retrieve": RetrieveLocationSerializer,
        "create": CreateLocationSerializer,
    }
