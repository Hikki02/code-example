from django.http import FileResponse
from rest_framework import viewsets, status, permissions, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.business_trips.models.business_trip_model import BUSINESS_TRIP_STATUSES
from utils.swagger.parameters import business_trip_activity_status

from apps.business_trips.models import BusinessTrip, PrimarySourceDocument,\
    BusinessTripCertificate, BusinessTripReport, AdvancedCostReport

from apps.business_trips.serializers import BusinessTripCompleteSerializer, PrimarySourceDocumentSerializer, \
    BusinessTripCertificateSerializer, BusinessTripReportSerializer, AdvancedCostReportSerializer

from apps.business_trips.services import BusinessTripService


class BusinessTripViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = BusinessTripCompleteSerializer
    service = BusinessTripService
    swagger_tags = ['Business Trip']

    def get_queryset(self):
        user = self.request.user
        business_trip_activity_status = self.request.query_params.get('status', None)
        queryset = BusinessTripService.get_business_trips_by_status(user, business_trip_activity_status)
        return queryset

    @swagger_auto_schema(manual_parameters=[business_trip_activity_status])
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        business_trip = self.service.get_by_id(object_id=pk)
        serializer = self.get_serializer(business_trip)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, permission_classes=[permissions.AllowAny])
    def get_status_counts(self, request, *args, **kwargs):
        counts = BusinessTripService.count_business_trips_by_status(request.user)
        return Response(counts, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, permission_classes=[permissions.AllowAny])
    def update_status_good(self, request, pk=None):
        business_trip = self.service.get_by_id(pk)
        status_transitions = {
            'awaiting_review': 'soon',
            'fix_required': 'awaiting_review',
            'submitting_docs': 'awaiting_advance_report',
            'awaiting_advance_report': 'awaiting_ao_check',
            'awaiting_ao_check': 'all_submitted',
            'need_docs_fix': 'awaiting_docs_check',
        }
        return self.service.update_business_trip_status(business_trip, status_transitions)

    @action(methods=['post'], detail=True, permission_classes=[permissions.AllowAny])
    def update_status_bad(self, request, pk=None):
        business_trip = self.service.get_by_id(pk)
        status_transitions = {
            'awaiting_review': 'fix_required',
            'fix_required': 'awaiting_review',
            'submitting_docs': 'need_docs_fix',
            'awaiting_ao_check': 'need_ao_fix',
        }
        return self.service.update_business_trip_status(business_trip, status_transitions)


class PrimarySourceDocumentViewSet(mixins.CreateModelMixin,
                                   mixins.RetrieveModelMixin,
                                   mixins.DestroyModelMixin,
                                   viewsets.GenericViewSet):
    """
    Создание, получение, удаление документов первички к определенной командировке
    """
    serializer_class = PrimarySourceDocumentSerializer
    queryset = PrimarySourceDocument.objects.all()
    swagger_tags = ['Primary Source Document']


class BusinessTripCertificateViewSet(mixins.CreateModelMixin,
                                     mixins.RetrieveModelMixin,
                                     mixins.DestroyModelMixin,
                                     viewsets.GenericViewSet):
    """
        Создание, получение, удаление командировочного удостоверения к определенной командировке
    """

    serializer_class = BusinessTripCertificateSerializer
    queryset = BusinessTripCertificate.objects.all()
    swagger_tags = ['Business Trip Certificate']

    @action(methods=['get'], detail=False, permission_classes=[permissions.AllowAny])
    def download_business_trip_certificate_template(self, request, *args, **kwargs):
        user = request.user

        file_path = BusinessTripService.get_certificate_template_for_user(user)
        file_name = "business_trip_certificate_template"

        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)


class BusinessTripReportViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    """
        Создание, получение, удаление отчета о командирвоке
    """

    serializer_class = BusinessTripReportSerializer
    queryset = BusinessTripReport.objects.all()
    swagger_tags = ['Business Trip Report']

    """
    Скачивание шаблона командировочного удостоверения. В зависимости от настроек компании, может быть скачан
    шаблон компании или шаблон по умолчанию.
    """

    @action(methods=['get'], detail=False, permission_classes=[permissions.AllowAny])
    def download_business_trip_report_template(self, request, *args, **kwargs):
        user = request.user
        file_path = BusinessTripService.get_report_template_for_user(user)
        file_name = "business_trip_report_template"

        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)


class AdvancedCostReportViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    """
        Создание, получение, удаление авансового отчета к определенной командировке
    """

    serializer_class = AdvancedCostReportSerializer
    queryset = AdvancedCostReport.objects.all()
    swagger_tags = ['Advanced Cost Report ']
