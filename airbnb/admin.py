from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    search_fields = ('name', 'host_name')
    

admin.site.register(Location, LocationAdmin)
admin.site.site_header = "Airbnb Location Risks"