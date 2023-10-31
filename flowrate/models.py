import uuid
from django.db import models

class Device(models.Model):
    serial_number = models.CharField(max_length=50, blank=True)
    device_owner = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "devices"

    def save(self, *args, **kwargs):
        if not self.serial_number: 
            self.serial_number = str(uuid.uuid4())[:8] 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.device_owner

class FlowRate(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    flow_rate = models.FloatField()

    class Meta:
        verbose_name_plural = "flowrates"