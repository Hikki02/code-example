from rest_framework.routers import SimpleRouter

from .views import CRMBusinessTripViewSet


crm_business_trips_router = SimpleRouter()

crm_business_trips_router.register(f'crm/crm_business_trip', CRMBusinessTripViewSet, basename='crm-business_trips')
