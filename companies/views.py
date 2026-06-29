from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySerializer, CompanyBriefSerializer
# Create your views here.

class CompanyListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        companies = Company.objects.filter(user=request.user)
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class CompanyDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        return Company.objects.get(
            pk=pk, 
            user=user
        )
    
    def get(self, request, pk):
        try:
            company = self.get_object(pk, request.user)
        except Company.DoesNotExist:
            return Response(
                {"detail":"Company not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    

    def post(self, request, pk):
        try:
            company = self.get_object(pk, request.user)
        except Company.DoesNotExist:
            return Response(
                {"detail":"Company not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = CompanySerializer(
            company,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
    

    def delete(self, request, pk):
        try:
            company = self.get_object(pk, request.user)
        except Company.DoesNotExist:
            return Response(
                {"detail":"Company not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)