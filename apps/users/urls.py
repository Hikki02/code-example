from django.urls import path
from rest_framework import routers
from apps.users.views import UserViewSet


user_router = routers.SimpleRouter()

user_router.register(r'user', UserViewSet, basename='users')
