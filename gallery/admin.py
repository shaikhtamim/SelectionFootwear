from django.contrib import admin
from .models import Gallery, GalleryImage


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "sort_order",
        "show_on_home",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_editable = (
        "show_on_home",
        "is_active",
        "sort_order",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [GalleryImageInline]