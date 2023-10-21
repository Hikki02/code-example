from django.utils import timezone

from tengri.celery import app
from .models import User


@app.task
def delete_unconfirmed_users():
    ten_minutes_ago = timezone.now() - timezone.timedelta(minutes=10)
    unconfirmed_users = User.objects.filter(is_active=False, created_at__lte=ten_minutes_ago)
    unconfirmed_users.delete()
