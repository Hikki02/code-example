from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import CompanySerializer


class CompanyCreateView(generics.CreateAPIView):
    """
    Создание компании
    """
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
