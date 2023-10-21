from django.contrib import admin

from .models import BusinessTrip, Accommodation, DailyAllowance, Transportation, BusinessTripCertificate, \
    BusinessTripReport, PrimarySourceDocument, AdvancedCostReport
from .filters import BusinessTripStatusFilter


@admin.register(BusinessTrip)
class BusinessTripAdmin(admin.ModelAdmin):
    list_filter = (BusinessTripStatusFilter, 'status')
    list_display = ('custom_trip_name', 'user', 'status')

    def custom_trip_name(self, obj):
        return f'Командировка #{obj.id}'

    custom_trip_name.short_description = 'ID'


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    ...


@admin.register(DailyAllowance)
class DailyAllowanceAdmin(admin.ModelAdmin):
    ...


@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    ...


@admin.register(BusinessTripCertificate)
class BusinessTripCertificateAdmin(admin.ModelAdmin):
    ...


@admin.register(BusinessTripReport)
class BusinessTripReportAdmin(admin.ModelAdmin):
    ...


@admin.register(PrimarySourceDocument)
class PrimarySourceDocumentAdmin(admin.ModelAdmin):
    ...


@admin.register(AdvancedCostReport)
class AdvancedCostReportAdmin(admin.ModelAdmin):
    ...
