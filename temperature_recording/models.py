from django.db import models
from device.models import Device

class TemperatureHumidityRecord(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)  
    temperature = models.DecimalField(max_digits=5, decimal_places=2) 

    @property
    def humidity_with_unit(self):
        return f"{self.humidity}% RH"

    @property
    def temperature_with_unit(self):
        return f"{self.temperature}°C"
