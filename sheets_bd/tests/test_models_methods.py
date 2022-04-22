import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "google_sheets_bd.settings")
django.setup()

from unittest import TestCase
from sheets_bd.functions.models_methods import start_create_clients_model, return_spreadsheet_data
from sheets_bd.models import Clients


class SoloFunctionsTestCase(TestCase):
    def test_return_spreadsheet_data(self):
        for index, client in enumerate(return_spreadsheet_data()['values'][5]):
            print(f'{client} ---- {index}')

    def test_create_clients_model(self):
        print(Clients.objects.all())
        start_create_clients_model()
        print(Clients.objects.all())
        # Clients.objects.all().delete()
