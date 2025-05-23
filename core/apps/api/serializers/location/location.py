from rest_framework import serializers

from core.apps.api.models import LocationModel


class BaseLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = [
            "id",
            "name",
            "long",
            "lat"
        ]


class ListLocationSerializer(BaseLocationSerializer):
    class Meta(BaseLocationSerializer.Meta): ...


class RetrieveLocationSerializer(BaseLocationSerializer):
    class Meta(BaseLocationSerializer.Meta): ...


class CreateLocationSerializer(BaseLocationSerializer):
    class Meta(BaseLocationSerializer.Meta):
        fields = [
            "id",
            "name",
            "long",
            "lat"
        ]
