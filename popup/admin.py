from django.contrib import admin
from .models import VisitorLead


@admin.register(VisitorLead)
class VisitorLeadAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "shop_name",
        "mobile",
        "device",
        "browser",
        "visit_count",
        "last_visit",
    )

    search_fields = (
        "name",
        "shop_name",
        "mobile",
        "ip_address",
    )

    list_filter = (
        "device",
        "browser",
        "operating_system",
        "created_at",
    )

    readonly_fields = (
        "ip_address",
        "browser",
        "device",
        "operating_system",
        "user_agent",
        "visit_count",
        "created_at",
        "last_visit",
    )