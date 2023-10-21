from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.companies.models import Company
from .serializers import CRMCompanyCreateSerializer, CRMCompanyLegalDocumentSerializer
from .services import CompanyService
from rest_framework import viewsets
from rest_framework import mixins


class CRMCompanyViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
                        ):
    serializer_class = CRMCompanyCreateSerializer
    queryset = Company.objects.filter()
    permission_classes = [permissions.AllowAny]
    swagger_tags = ['CRM Company']

    def create(self, request, *args, **kwargs):
        serializer = CRMCompanyCreateSerializer(data=request.data)
        if serializer.is_valid():
            sysadmin_email = request.user.email
            company = CompanyService.create_company(sysadmin_email=sysadmin_email, **serializer.validated_data)
            request.user.company = company
            request.user.save()

            company_serializer = CRMCompanyCreateSerializer(company)

            return Response({
                "message": "Company created successfully",
                "status": status.HTTP_201_CREATED,
                "company": company_serializer.data
            })

        return Response({
            "message": "Bad request",
            "status": status.HTTP_400_BAD_REQUEST,
            "errors": serializer.errors
        })
    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def upload_legal_document(self, request, *args, **kwargs):
        user = request.user
        # company = CompanyService.get_user_company(user)

        company = user.company

        if not company:
            return Response({"message": "User is not associated with any company.", "status": status.HTTP_404_NOT_FOUND})

        serializer = CRMCompanyLegalDocumentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data['company'] = company
            serializer.save()
            return Response({"message": "Legal document uploaded successfully", "status": status.HTTP_201_CREATED, "document": serializer.data})
        return Response({"message": "Bad request", "status": status.HTTP_400_BAD_REQUEST})
