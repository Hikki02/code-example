from django.contrib.admin import SimpleListFilter


class BusinessTripStatusFilter(SimpleListFilter):
    title = 'Статус командировок'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('completed', 'Завершенные командировки'),
            ('active', 'Активные командировки'),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'completed':
            return queryset.filter(status__in=['all_submitted', 'cancel'])
        elif value == 'active':
            return queryset.exclude(status__in=['all_submitted', 'cancel'])






