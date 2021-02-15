from django.contrib import admin

from .models import Portfolio, Screenshot


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'live_url', 'source_url', 'port_type']
    list_filter = ['created', 'updated']
    search_fields = ['title', 'description']


class ScreenshotAdmin(admin.ModelAdmin):
    list_filter = ['portfolio', ]


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Screenshot, ScreenshotAdmin)
