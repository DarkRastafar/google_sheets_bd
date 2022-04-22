from django.contrib import admin

from sheets_bd.admin_extends.fieldsets import clients_fieldsets
from sheets_bd.admin_extends.lists_displat import full_list_display
from sheets_bd.models import Clients


class ParentClientsAdmin(admin.ModelAdmin):
    list_display = ['id'] + full_list_display
    list_per_page = 5
    fieldsets = clients_fieldsets


@admin.register(Clients)
class ClientsAdmin(ParentClientsAdmin):
    pass
