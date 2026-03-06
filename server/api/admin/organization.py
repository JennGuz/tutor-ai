from django.contrib import admin
from api.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'enabled', 'created_at')
    list_filter = ('enabled',)
