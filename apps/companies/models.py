from django.db import models

from utils.base.base_model import BaseModel


class CompanyLegalDocument(BaseModel):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='Компания')
    file = models.FileField(upload_to='legal_documents/', verbose_name='Скан оригинала документа')

    class Meta:
        verbose_name = 'Скан оригинала документа'
        verbose_name_plural = 'Сканы оригиналов документов'

    def __str__(self):
        return f'{self.company.name} - {self.file.name}'


class Company(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='company_user')
    bin = models.BigIntegerField(verbose_name='БИН', unique=True)
    name = models.CharField(max_length=225, verbose_name='Название компании')
    legal_address = models.CharField(max_length=225, verbose_name='Юридический адрес', default=None, null=True)
    ceo_name = models.CharField(max_length=225, verbose_name='Имя генерального директора', default=None, null=True)
    sysadmin_email = models.EmailField(verbose_name='Email системного администратора', null=True, blank=True)
    certificate_template = models.FileField(upload_to='certificate_templates/', null=True, blank=True, default=None,
                                            verbose_name='Шаблон командировочного удостоверения')
    advanced_cost_report_template = models.FileField(upload_to='advanced_cost_report_templates/', null=True,
                                                     blank=True, default=None,
                                                     verbose_name='Шаблон авансового отчета')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name
