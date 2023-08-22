from django.contrib import admin
from .models import Employees, Logs, Daily_attendance
# Register your models here.

class EmployeesAdminPage(admin.ModelAdmin):
    list_display = ('username', 'employee_id', 'position', 'created_at',)
    list_display_links = ('employee_id', 'username',)  # Make the name column clickable

class LogsAdminPage(admin.ModelAdmin):
    list_display = ('user', 'recognition_time', 'conf_level',)

class DailyAdminPage(admin.ModelAdmin):
    list_display = ('user','entry_time', 'exit_time',)


admin.site.register(Employees, EmployeesAdminPage)
admin.site.register(Logs, LogsAdminPage)
admin.site.register(Daily_attendance, DailyAdminPage)