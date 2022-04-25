from config import BANK_LIST
from sheets_bd.models import Clients


def check_field(field):
    for bank in BANK_LIST:
        if field.startswith(bank):
            return False
    else:
        return True


def return_model_fields(bank: str = None):
    if bank is None:
        return [field.name for field in Clients._meta.get_fields() if check_field(field.name) is True]
    elif bank in BANK_LIST:
        return [field.name for field in Clients._meta.get_fields() if bank in field.name]


alfabank_list_display = return_model_fields('alfa')
vtb_list_display = return_model_fields('vtb')
tinkoff_list_display = return_model_fields('tinkoff')
otkritie_list_display = return_model_fields('otkritie')
tochka_list_display = return_model_fields('tochka')
psb_list_display = return_model_fields('psb')
module_list_display = return_model_fields('module')
main_list_display = return_model_fields()


full_list_display = main_list_display + alfabank_list_display + vtb_list_display + tinkoff_list_display + \
                    otkritie_list_display + tochka_list_display + psb_list_display + module_list_display + \
                    ['date_create_client']
