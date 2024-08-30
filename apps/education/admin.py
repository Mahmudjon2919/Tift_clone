from django.contrib import admin
from apps.education import models


@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number")