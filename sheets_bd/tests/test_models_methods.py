import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "google_sheets_bd.settings")
django.setup()

from unittest import TestCase
from sheets_bd.functions.models_methods import return_spreadsheet_data


class SoloFunctionsTestCase(TestCase):
    def test_return_spreadsheet_data(self):
        test_res = return_spreadsheet_data()
        print(test_res)
        print(type(test_res))
