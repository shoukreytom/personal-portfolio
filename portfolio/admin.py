from django.contrib import admin
from portfolio.models import Portfolio, Screenshot, Tool


class EmbeddedScreenshot(admin.TabularInline):
    model = Screenshot
    extra = 1


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'live_url', 'source_url', 'port_type']
    list_filter = ['created', 'updated']
    search_fields = ['title', 'description']
    inlines = [EmbeddedScreenshot, ]


@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_filter = ['portfolio', ]


admin.site.register(Tool)
