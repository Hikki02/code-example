from django.utils import timezone

from tengri.celery import app
from .models import BusinessTrip


@app.task
def update_soon_status_task():
    business_requests = BusinessTrip.objects.filter(status='soon', departure_date=timezone.now().date())

    for business_request in business_requests:
        business_request.status = 'in_trip'
        business_request.save()
