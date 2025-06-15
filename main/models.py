from django.db import models

class ApplicationSetting(models.Model):
    config_key = models.CharField(max_length=100)
    config_value = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'application_settings'  # Chính xác tên bảng trong MySQL

    def __str__(self):
        return f"{self.config_key}: {self.config_value}"
