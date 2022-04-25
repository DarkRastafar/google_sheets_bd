import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "google_sheets_bd.settings")
django.setup()

from unittest import TestCase
from sheets_bd.functions.models_methods import (start_create_clients_model, return_spreadsheet_data,
                                                create_sheet_responses, create_kwargs_client)
from sheets_bd.models import Clients, SheetsResponses, RangeModel


class SoloFunctionsTestCase(TestCase):
    def test_return_spreadsheet_data(self):
        print(return_spreadsheet_data()['values'][5])
        # for index, client in enumerate(return_spreadsheet_data()['values'][5]):
        #     print(f'{client} ---- {index}')

    def test_create_sheet_responses(self):
        print(RangeModel.objects.all())
        print(SheetsResponses.objects.all())
        create_sheet_responses()

        print(RangeModel.objects.all())
        print(SheetsResponses.objects.all())

    def test_create_clients_model(self):
        print(Clients.objects.all())
        start_create_clients_model()
        print(Clients.objects.all())
        # Clients.objects.all().delete()

    def test_delete_all(self):
        Clients.objects.all().delete()

    def test_test(self):
        def r(t, y, u):
            print(t, y, u)

        d = {'t': 1, 'y': 2, 'u': 3}

        r(**d)

    def test_create_kwargs_client(self):
        client = ['9718186848', 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ЛОГФИНСОФТ"', 'КОРОЛЕВА', 'МАРИНА', 'ВЯЧЕСЛАВОВНА', '79260115044', '107258, ГОРОД МОСКВА, , , , БУЛЬВАР МАРШАЛА РОКОССОВСКОГО, 39/22, , 128', 'МОСКВА', '', '', '1', 'TRUE', '', '', '', '', '', '', '', 'Москва', '', '0c5b2444-70a0-4932-980c-b4dc0d3f02b5', '', '', '', '', '', '', '', '', '', 'TRUE', '', 'Москва', '4', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'success', '', '', '', '', 'Москва', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Москва', '', '1']
        test_res = create_kwargs_client(client)
        print(test_res)
        print(type(test_res))

    def test_return_fields(self):
        exception_list = ['id', 'range_field']
        field_name_list = [field.name for field in Clients._meta.get_fields() if field.name not in exception_list]
        print(field_name_list)
