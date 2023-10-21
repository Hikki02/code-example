from django.core.exceptions import PermissionDenied

from apps.business_trips.services import BusinessTripService


class CrmBusinessTripService(BusinessTripService):
    @classmethod
    def get_all_by_user_company(cls, user):
        if user.is_anonymous:
            raise PermissionDenied("Вы должны авторизоваться, чтобы просматривать список командировок.")
        company = user.company
        return cls.model.objects.filter(user__company=company)
