from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.models import User
from crm.users.serializers import (
    EmployeeCreateSerializer,
    EmployeeListSerializer,
    EmployeeUpdateSerializer,
)



class CRMUserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = EmployeeCreateSerializer
    swagger_tags = ['CRM User']

    def get_queryset(self):
        company = self.request.user.company
        return User.objects.filter(company=company)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_employee = serializer.create(serializer.validated_data)

        user_admin = request.user
        company = user_admin.company
        user_employee.company = company
        user_employee.is_active = True
        user_employee.save()

        return Response({"message": "Employee created successfully", "status": status.HTTP_201_CREATED,
                         "employee": serializer.data})
