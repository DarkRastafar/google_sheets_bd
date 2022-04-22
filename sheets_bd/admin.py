from django.contrib import admin

from sheets_bd.admin_extends.fieldsets import clients_fieldsets
from sheets_bd.admin_extends.lists_displat import full_list_display
from sheets_bd.models import Clients, SheetsResponses, RangeModel


class ParentClientsAdmin(admin.ModelAdmin):
    list_display = ['id'] + full_list_display
    list_per_page = 5
    fieldsets = clients_fieldsets


class SheetsResponsesInline(admin.TabularInline):
    model = SheetsResponses
    extra = 0


@admin.register(RangeModel)
class RangeModelAdmin(admin.ModelAdmin):
    list_display = ['range_field']
    list_per_page = 5
    inlines = [SheetsResponsesInline]


@admin.register(Clients)
class ClientsAdmin(ParentClientsAdmin):
    pass


@admin.register(SheetsResponses)
class SheetsResponsesAdmin(admin.ModelAdmin):
    list_display = ['range_field', 'response']
    list_per_page = 5
