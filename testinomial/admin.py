from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    # Display columns in Admin list view
    list_display = (
        'id', 
        'name', 
        'location', 
        'review_rate', 
        'is_active', 
        'sort_order', 
        'created_at'
    )
    
    # Enable instant edits straight from the list table
    list_editable = ('is_active', 'sort_order', 'review_rate')
    
    # Filter options on the right sidebar
    list_filter = ('is_active', 'review_rate', 'created_at')
    
    # Search bar capability
    search_fields = ('name', 'location', 'description')
    
    # Grouping fields cleanly inside the Admin Edit form
    fieldsets = (
        ('Customer Details', {
            'fields': ('name', 'location', 'image')
        }),
        ('Review Content', {
            'fields': ('review_rate', 'description')
        }),
        ('Visibility & Ordering', {
            'fields': ('is_active', 'sort_order')
        }),
    )