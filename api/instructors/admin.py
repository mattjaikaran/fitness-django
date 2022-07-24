from django.contrib import admin
from .models import Instructor


class InstructorAdmin(admin.ModelAdmin):
    list_filter = ("email", "is_active")


admin.site.register(Instructor, InstructorAdmin)
