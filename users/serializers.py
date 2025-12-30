from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    created_orders = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)
    updated_orders = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)
    uploaded_images = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)
    deleted_images = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'