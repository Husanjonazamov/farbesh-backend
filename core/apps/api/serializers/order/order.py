from rest_framework import serializers

from core.apps.api.models import OrderModel


class BaseOrderSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    class Meta:
        model = OrderModel
        fields = [
            "id",
            "name",
            "location",
            "phone",
            "gender",
            "count"
        ]


    def get_location(self, obj):
        from core.apps.api.serializers.location import ListLocationSerializer
        return ListLocationSerializer(obj.location).data

class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(serializers.ModelSerializer):
    location = serializers.DictField(write_only=True)
    class Meta:
        model = OrderModel
        fields = [
            'id',
            'name',
            'phone',
            'location',
            'gender',
            'count'
        ]
        
    def create(self, validate_data):
        location_data = validate_data.pop("location")
        from core.apps.api.models import LocationModel
        
        location = LocationModel.objects.create(**location_data)
        order = OrderModel.objects.create(location=location, **validate_data)
        return order

         
