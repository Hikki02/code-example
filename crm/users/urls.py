from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CRMUserViewSet


crm_user_router = SimpleRouter()

crm_user_router.register(f'crm/crm_user', CRMUserViewSet, basename='crm_user')
