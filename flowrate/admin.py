from django.contrib import admin
from .models import FlowRate, Device

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'device_owner')

admin.site.register(Device, DeviceAdmin)

class FlowRateAdmin(admin.ModelAdmin):
    list_display = ('device', 'time_stamp', 'flow_rate')

admin.site.register(FlowRate, FlowRateAdmin)