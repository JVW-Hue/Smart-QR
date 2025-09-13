from django.contrib import admin
from .models import QRCode

@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'color', 'is_paid', 'created_at']
    list_filter = ['is_paid', 'created_at']
    search_fields = ['content']
    readonly_fields = ['id', 'created_at']