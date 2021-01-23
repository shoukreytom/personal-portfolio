from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Portfolio, Screenshot


class PortfolioAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ['description', ]
    list_display = ['title', 'description', 'url', 'port_type']
    list_filter = ['created', 'updated']
    search_fields = ['title', 'description']
    prepopulated_fields = {
        'slug': ['title']
    }


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Screenshot)
