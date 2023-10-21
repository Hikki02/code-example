"""
URL configuration for tengri project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.urls import user_router
from crm.business_trips.urls import crm_business_trips_router
from crm.users.urls import crm_user_router
from apps.business_trips.urls import business_trips, business_trip_report,\
    business_trip_certificate, business_trips_advanced_cost_report,\
    business_trips_primary_source_document

from tengri.settings import development

from crm.companies.urls import crm_company_router

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="tengri",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = SimpleRouter()
router.registry.extend(business_trips_primary_source_document.registry)
router.registry.extend(business_trip_certificate.registry)
router.registry.extend(business_trip_report.registry)
router.registry.extend(business_trips.registry)
router.registry.extend(business_trips_advanced_cost_report.registry)
router.registry.extend(user_router.registry)


crm_v1_router = SimpleRouter()
crm_v1_router.registry.extend(crm_company_router.registry)
crm_v1_router.registry.extend(crm_business_trips_router.registry)
crm_v1_router.registry.extend(crm_user_router.registry)

urlpatterns = [
    path('api/', include(crm_v1_router.urls)),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/user/refresh_token/', TokenRefreshView.as_view()),
    path('api/companies/', include('apps.companies.urls')),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static(development.STATIC_URL, document_root=development.STATIC_ROOT)
urlpatterns += static(development.MEDIA_URL, document_root=development.MEDIA_ROOT)
