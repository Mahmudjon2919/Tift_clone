from django.contrib import admin
from apps.application.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "password", "status")
    list_editable = ("status", )
