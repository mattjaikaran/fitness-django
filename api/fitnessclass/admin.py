from django.contrib import admin
from .models import FitnessClass


class FitnessClassAdmin(admin.ModelAdmin):
    list_filter = ("location", "instructor", "room")


admin.site.register(FitnessClass, FitnessClassAdmin)
