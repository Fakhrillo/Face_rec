from rest_framework import serializers
from .models import Employees, Logs, Daily_attendance

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'

class Daily_attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily_attendance
        fields = '__all__'