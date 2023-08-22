from django.urls import path
from .views import EmployeesListCreateView, LogsLitsCreateView, Daily_attendanceListCreateView, user_logs

urlpatterns = [
    path('employees/', EmployeesListCreateView.as_view(), name='employees'),
    path('logs/', LogsLitsCreateView.as_view(), name='logs'),
    path('daily/', Daily_attendanceListCreateView.as_view(), name='daily_attendance'),
    path('logs/<int:user_id>/<str:log_date>/', user_logs, name='user_logs'),
]