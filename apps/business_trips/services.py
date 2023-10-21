from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.business_trips.models import BusinessTrip
from apps.business_trips.models.business_trip_model import BUSINESS_TRIP_STATUSES
from utils.base.base_service import BaseService
from django.http import JsonResponse

ACTIVE_STATUSES = [
    'awaiting_review',
    'fix_required',
    'soon',
    'in_trip',
    'submitting_docs',
    'awaiting_docs_check',
    'need_docs_fix',
    'awaiting_advance_report',
    'awaiting_ao_check',
    'need_ao_fix'
]
COMPLETED_STATUSES = [
    'all_submitted',
    'cancellation'
]


class BusinessTripService(BaseService):
    model = BusinessTrip

    @classmethod
    def create_business_trip(cls, **kwargs):
        try:
            business_trip = cls.create(**kwargs)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return business_trip

    @classmethod
    def update_business_trip(cls, object_id, **kwargs):
        try:
            business_trip = cls.update(object_id, **kwargs)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return business_trip

    @classmethod
    def update_business_trip_status(cls, business_trip, status_transitions):
        if business_trip.status in status_transitions:
            next_status = status_transitions[business_trip.status]
            business_trip.status = next_status
            business_trip.save()
            return JsonResponse({'message': 'Статус успешно обновлен'})
        else:
            return JsonResponse({'message': 'Статус не может быть обновлен'})

    @classmethod
    def get_certificate_template_for_user(cls, user):
        if user.company and user.company.certificate_template:
            return user.company.certificate_template.path
        else:
            return "templates/certificate_template.docx"

    @classmethod
    def get_report_template_for_user(cls, user):
        if user.company and user.company.advanced_cost_report_template:
            return user.company.advanced_cost_report_template.path
        else:
            return "templates/advanced_cost_report_template.docx"

    @classmethod
    def get_business_trips_by_status(cls, user, status=None):
        if status == 'active':
            queryset = BusinessTrip.objects.filter(user=user, status__in=ACTIVE_STATUSES)
        elif status == 'completed':
            queryset = BusinessTrip.objects.filter(user=user, status__in=COMPLETED_STATUSES)
        else:
            queryset = BusinessTrip.objects.filter(user=user)
        return queryset

    @classmethod
    def count_business_trips_by_status(cls, user):
        counts = {
            'active': 0,
            'completed': 0
        }

        for trip_status, _ in BUSINESS_TRIP_STATUSES:
            count = BusinessTrip.objects.filter(status=trip_status, user=user).count()

            if trip_status in ACTIVE_STATUSES:
                counts['active'] += count
            elif trip_status in COMPLETED_STATUSES:
                counts['completed'] += count
        return counts
