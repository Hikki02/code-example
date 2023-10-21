from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CRMCompanyViewSet

crm_company_router = SimpleRouter()

crm_company_router.register(f'crm/crm_company', CRMCompanyViewSet, basename='crm-company')
