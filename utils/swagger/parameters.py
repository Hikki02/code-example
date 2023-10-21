from drf_yasg import openapi

from apps.business_trips.models.business_trip_model import BUSINESS_TRIP_STATUSES, DAILY_ALLOWANCE_STATUSES

token = openapi.Parameter(
    'token',
    openapi.IN_QUERY,
    description='Token that send in email',
    required=False,
    type=openapi.TYPE_STRING
)


uidb64 = openapi.Parameter(
    'uidb64',
    openapi.IN_QUERY,
    description='Token that send in email',
    required=False,
    type=openapi.TYPE_STRING
)

business_trip_activity_status = openapi.Parameter(
    'status',
    openapi.IN_QUERY,
    description='Filter by status',
    required=False,
    type=openapi.TYPE_STRING,
    enum=['active', 'completed']
)

is_approved = openapi.Parameter(
    'is_approved',
    openapi.IN_QUERY,
    description='Filter by is_approved',
    required=False,
    type=openapi.TYPE_BOOLEAN,
    enum=[True, False]
)

employee_name = openapi.Parameter(
    'employee_name',
    openapi.IN_QUERY,
    description='Filter by employee_name',
    required=False,
    type=openapi.TYPE_STRING,
)

destination_place = openapi.Parameter(
    'destination_place',
    openapi.IN_QUERY,
    description='Filter by destination_place',
    required=False,
    type=openapi.TYPE_STRING,
)

departure_place = openapi.Parameter(
    'departure_place',
    openapi.IN_QUERY,
    description='Filter by departure_place',
    required=False,
    type=openapi.TYPE_STRING,
)

business_trip_status = openapi.Parameter(
    'business_trip_status',
    openapi.IN_QUERY,
    description='Filter by business_trip_status',
    required=False,
    type=openapi.TYPE_STRING,
    enum=BUSINESS_TRIP_STATUSES,
)

start_date = openapi.Parameter(
    'start_date',
    openapi.IN_QUERY,
    description='Filter by start_date. Format: YYYY-MM-DD',
    required=False,
    type=openapi.TYPE_STRING,
)

end_date = openapi.Parameter(
    'end_date',
    openapi.IN_QUERY,
    description='Filter by end_date. Format: YYYY-MM-DD',
    required=False,
    type=openapi.TYPE_STRING,
)

daily_allowance_status = openapi.Parameter(
    'daily_allowance_status',
    openapi.IN_QUERY,
    description='Filter by daily_allowance_status',
    required=False,
    type=openapi.TYPE_STRING,
    enum=DAILY_ALLOWANCE_STATUSES
)
