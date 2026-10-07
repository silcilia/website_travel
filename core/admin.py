from django.contrib import admin
from .models import BookingInquiry


@admin.register(BookingInquiry)
class BookingInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'package', 'created_at')
    list_filter = ('package', 'created_at')
    search_fields = ('name', 'phone', 'message')
    readonly_fields = ('created_at',)
