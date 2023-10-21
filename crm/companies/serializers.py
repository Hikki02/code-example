from rest_framework import serializers
from apps.companies.models import Company, CompanyLegalDocument


class CRMCompanyLegalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyLegalDocument
        fields = (
            'id',
            'company',
            'file',
        )


class CRMCompanyCreateSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = (
            'id',
            'bin',
            'name',
            'user',
            'legal_address',
            'ceo_name',
            'sysadmin_email',
            'certificate_template',
            'advanced_cost_report_template',
        )
