from django import forms

from core.apps.api.models import OrderModel


class OrderForm(forms.ModelForm):

    class Meta:
        model = OrderModel
        fields = "__all__"
