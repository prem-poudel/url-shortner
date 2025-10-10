from django.contrib import admin
from .models import ShortLink

@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_code', 'original_url', 'user', 'clicks', 'created_at')
    search_fields = ('short_code', 'original_url', 'user__username', 'user__email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('clicks', 'created_at', 'short_code')