from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'bin', 'name', 'legal_address', 'ceo_name', 'sysadmin_email', 'certificate_template',
                  'advanced_cost_report_template')
