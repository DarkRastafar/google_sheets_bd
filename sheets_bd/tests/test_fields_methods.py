import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "google_sheets_bd.settings")
django.setup()

from unittest import TestCase
from sheets_bd.functions.fields_methods import (return_model_fields, return_mutation_client,
                                                create_kwargs_client, create_kwargs_banks)
from config import BANK_LIST


class SoloFunctionsTestCase(TestCase):
    def setUp(self):
        self.client = ['718186848', 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ЛОГФИНСОФТ"', 'КОРОЛЕВА', 'МАРИНА',
                  'ВЯЧЕСЛАВОВНА', '79260115044',
                  '107258, ГОРОД МОСКВА, , , , БУЛЬВАР МАРШАЛА РОКОССОВСКОГО, 39/22, , 128', 'МОСКВА', '', '', '1',
                  'TRUE', '', '', '', '', '', '', '', 'Москва', '', '0c5b2444-70a0-4932-980c-b4dc0d3f02b5', '', '', '',
                  '', '', '', '', '', '', 'TRUE', '', 'Москва', '4', '', '', '', '', '', '', '', '', '', '', '', '', '',
                  '', '', '', '', '', 'success', '', '', '', '', 'Москва', '', '', '', '', '', '', '', '', '', '', '',
                  '', '', '', '', '', '', '', '', '', '', 'Москва', '', '1']

    def test_return_model_fields(self):
        test_res = return_model_fields('alfa')
        print(test_res)
        print(type(test_res))

    def test_mutation_client(self):
        client = ['718186848', 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ЛОГФИНСОФТ"', 'КОРОЛЕВА', 'МАРИНА',
                  'ВЯЧЕСЛАВОВНА', '79260115044',
                  '107258, ГОРОД МОСКВА, , , , БУЛЬВАР МАРШАЛА РОКОССОВСКОГО, 39/22, , 128', 'МОСКВА', '', '', '1',
                  'TRUE', '', '', '', '', '', '', '', 'Москва', '', '0c5b2444-70a0-4932-980c-b4dc0d3f02b5', '', '', '',
                  '', '', '', '', '', '', 'TRUE', '', 'Москва', '4', '', '', '', '', '', '', '', '', '', '', '', '', '',
                  '', '', '', '', '', 'success', '', '', '', '', 'Москва', '', '', '', '', '', '', '', '', '', '', '',
                  '', '', '', '', '', '', '', '', '', '', 'Москва', '', '1']
        print(len(client))
        test_res = return_mutation_client(client)
        print(test_res)
        print(len(client))
        print(client[95])

    def test_create_kwargs_client(self):
        test_res = create_kwargs_client(return_mutation_client(self.client))
        print(test_res)
        print(type(test_res))

    def test_create_kwargs_banks(self):
        banks = BANK_LIST
        test_res = create_kwargs_banks(return_mutation_client(self.client), banks)
        print(test_res)
        print(type(test_res))
