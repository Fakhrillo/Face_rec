from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployeesSerializer, LogsSerializer, Daily_attendanceSerializer
from .models import Employees, Logs, Daily_attendance
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.dateparse import parse_date
from datetime import datetime
# Create your views here.

class EmployeesListCreateView(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class LogsLitsCreateView(generics.ListCreateAPIView):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer

class Daily_attendanceListCreateView(generics.ListCreateAPIView):
    queryset = Daily_attendance.objects.all()
    serializer_class = Daily_attendanceSerializer

@api_view(['GET'])
def user_logs(request, user_id, log_date):
    try:
        date_obj = parse_date(log_date)
        logs = Logs.objects.filter(user__id=user_id, recognition_time__date=date_obj)
        serializer = LogsSerializer(logs, many=True)  # Serialize the logs
        return Response(serializer.data)
    except Logs.DoesNotExist:
        return Response(status=404)