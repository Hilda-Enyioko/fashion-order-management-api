from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    orders = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='order-detail'
    )

    class Meta:
        model = Customer
        fields = '__all__'

# NOTE: A url pattern named 'order-detail' needs to be created in the project's URL configuration for the HyperlinkedRelatedField to function correctly.