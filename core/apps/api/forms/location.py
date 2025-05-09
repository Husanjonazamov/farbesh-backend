from django import forms

from core.apps.api.models import LocationModel


class LocationForm(forms.ModelForm):

    class Meta:
        model = LocationModel
        fields = "__all__"
