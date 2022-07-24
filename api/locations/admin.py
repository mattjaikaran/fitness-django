from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    list_filter = "name"


admin.site.register(Location, LocationAdmin)
