
from django.contrib import admin
from .models import Device  

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number')  
    readonly_fields = ('serial_number',) 
admin.site.register(Device, DeviceAdmin)
