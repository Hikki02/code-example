from django.contrib import admin

from apps.companies.models import Company, CompanyLegalDocument


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    ...


@admin.register(CompanyLegalDocument)
class CompanyLegalDocumentAdmin(admin.ModelAdmin):
    ...
