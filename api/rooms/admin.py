from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_filter = ("name", "location")


admin.site.register(Room, RoomAdmin)
