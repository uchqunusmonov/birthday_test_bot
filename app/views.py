from django.shortcuts import render
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from .models import TelegramUser, Employee
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import TelegramUserSerializer, EmployeeSerializer, TelegramAdminSerializer

today = datetime.now().today().date()


class TelegramUserCreateAPIView(APIView):
    def get(self, request):
        user = TelegramUser.objects.all()
        serializer = TelegramUserSerializer(user, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        try:
            instance = TelegramUser.objects.get(user_id=user_id)
            serializer = TelegramUserSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except TelegramUser.DoesNotExist:
            serializer = TelegramUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeesBirthdayAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.filter(
            birthday__month=today.month,
            birthday__day=today.day
        )
        return queryset


class TelegramAdminsListAPIView(ListAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramAdminSerializer

    def get_queryset(self):
        queryset = TelegramUser.objects.filter(
            is_admin=True
        )
        return queryset


