
from rest_framework import routers

from apps.business_trips.views import BusinessTripViewSet, BusinessTripCertificateViewSet,\
    BusinessTripReportViewSet, PrimarySourceDocumentViewSet, AdvancedCostReportViewSet


business_trips = routers.SimpleRouter()
business_trips.register(r'business_trip', BusinessTripViewSet, basename='business_trips')


business_trip_certificate = routers.SimpleRouter()
business_trip_certificate.register(f'business_trip/certificate', BusinessTripCertificateViewSet, basename='business_trip_certificate')


business_trip_report = routers.SimpleRouter()
business_trip_report.register('business_trip/report', BusinessTripReportViewSet, basename='business_trip_report')


business_trips_primary_source_document = routers.SimpleRouter()
business_trips_primary_source_document.register('business_trip/primary_source_document', PrimarySourceDocumentViewSet,
                                                basename='business_trip_primary_source_document')


business_trips_advanced_cost_report = routers.SimpleRouter()
business_trips_advanced_cost_report.register('business_trip/advanced_cost_report', AdvancedCostReportViewSet,
                                             basename='business_trips_advanced_cost_report')
