from django.contrib import admin
from .models import TemperatureHumidityRecord

# Register your models here.
class  TemperatureHumidityRecordAdmin(admin.ModelAdmin):
    list_display = ('time_stamp','humidity','temperature')

admin.site.register(TemperatureHumidityRecord,TemperatureHumidityRecordAdmin)
