import django_filters
from django.db.models import Q

from apps.business_trips.models import BusinessTrip
from apps.business_trips.models.business_trip_model import BUSINESS_TRIP_STATUSES, DAILY_ALLOWANCE_STATUSES


class BusinessTripFilter(django_filters.FilterSet):
    # Фильтр по статусу одобрения бухгатером заявки на командировку
    is_approved = django_filters.BooleanFilter(field_name='is_approved')

    # Фильтр по имени и фамилии сотрудника
    employee_name = django_filters.CharFilter(method='filter_employee_name')

    # Фильтр по месту назначения (городу или стране)
    destination_place = django_filters.CharFilter(method='filter_destination_place')

    # Фильтр по месту отправления (городу или стране)
    departure_place = django_filters.CharFilter(method='filter_departure_place')

    # Фильтр по статусам командировок
    business_trip_status = django_filters.MultipleChoiceFilter(choices=BUSINESS_TRIP_STATUSES)

    # Фильтр по периоду от какого-то числа до какого-то числа
    start_date = django_filters.DateFilter(field_name='departure_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='return_date', lookup_expr='lte')

    # Фильтр по статусу суточных
    daily_allowance_status = django_filters.ChoiceFilter(choices=DAILY_ALLOWANCE_STATUSES)

    class Meta:
        model = BusinessTrip
        fields = []

    def filter_employee_name(self, queryset, name, value):
        names = value.split()
        first_name = names[0] if len(names) > 0 else ''
        last_name = names[-1] if len(names) > 0 else ''

        q = Q()

        if first_name:
            q |= Q(user__first_name__icontains=first_name)
        if last_name:
            q |= Q(user__last_name__icontains=last_name)

        return queryset.filter(q)

    def filter_destination_place(self, queryset, name, value):
        q = Q()

        q |= Q(destination_country__icontains=value)
        q |= Q(destination_city__icontains=value)

        return queryset.filter(q)

    def filter_departure_place(self, queryset, name, value):
        q = Q()

        q |= Q(departure_country__icontains=value)
        q |= Q(departure_city__icontains=value)

        return queryset.filter(q)
