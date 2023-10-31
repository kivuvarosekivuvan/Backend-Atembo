from django.contrib import admin
from .models import Location  


class LocationAdmin(admin.ModelAdmin):
    list_display = ('region_name', 'installation_date', 'updated_at')
    list_filter = ('installation_date', 'updated_at')
    search_fields = ('region_name',)
admin.site.register(Location,LocationAdmin)