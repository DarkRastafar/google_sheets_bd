import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "google_sheets_bd.settings")
django.setup()

from unittest import TestCase
from sheets_bd.functions.fields_methods import return_model_fields


class SoloFunctionsTestCase(TestCase):
    def test_return_model_fields(self):
        test_res = return_model_fields('alfa')
        print(test_res)
        print(type(test_res))
