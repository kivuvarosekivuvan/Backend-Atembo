from django.contrib import admin
from .models import TemperatureHumidityRecord

class TemperaturehumidityAdmin(admin.ModelAdmin):
    list_temperature_humidity = ( "time_stamp", "humidity","temperature")
admin.site.register(TemperatureHumidityRecord ,TemperaturehumidityAdmin)