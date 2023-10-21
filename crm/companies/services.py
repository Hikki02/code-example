
from apps.companies.models import Company
from utils.base.base_service import BaseService


class CompanyService(BaseService):
    model = Company

    @classmethod
    def create_company(cls, sysadmin_email, **kwargs):
        kwargs['sysadmin_email'] = sysadmin_email
        return cls.create(**kwargs)

    @classmethod
    def update_company(cls, company_id, **kwargs):
        return cls.update(company_id, **kwargs)

    @classmethod
    def delete_company(cls, company_id):
        return cls.delete(company_id)

    @classmethod
    def get_user_company(cls, user):
        try:
            return cls.model.objects.get(user=user)
        except cls.model.DoesNotExist:
            return None
