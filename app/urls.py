from django.urls import path
from .views import *

urlpatterns = [
    path('users/', TelegramUserCreateAPIView.as_view()),
    path('employees/', EmployeeListAPIView.as_view()),
    path('birthdays/', EmployeesBirthdayAPIView.as_view()),
    path('admins/', TelegramAdminsListAPIView.as_view())
]
