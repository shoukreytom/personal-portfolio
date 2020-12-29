from django.contrib import admin

from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'url', 'port_type']
    list_filter = ['created', 'updated']
    search_fields = ['title', 'description']
    prepopulated_fields = {
        'slug': ['title']
    }


admin.site.register(Portfolio, PortfolioAdmin)
