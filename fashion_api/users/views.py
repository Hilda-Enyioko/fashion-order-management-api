from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from .models import User
from .permissions import GeneralPermissions, UserPermissions
from .serializers import UserSerializer

# Create your views here.
@extend_schema(tags=['User'])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all
    serializer_class = UserSerializer
    permission_classes = [GeneralPermissions, UserPermissions]
    