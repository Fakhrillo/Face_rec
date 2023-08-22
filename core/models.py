from django.db import models

# Create your models here.
class Employees(models.Model):
    employee_id = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.username

class Logs(models.Model):
    user = models.ForeignKey(Employees, on_delete=models.CASCADE)
    recognition_time = models.DateTimeField()
    conf_level = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Logs"

class Daily_attendance(models.Model):
    user = models.ForeignKey(Employees, on_delete=models.CASCADE)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Daily_attendance"