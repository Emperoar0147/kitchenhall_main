from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    model = Order
    fields = "__all__"

    class Meta:
        proxy = True