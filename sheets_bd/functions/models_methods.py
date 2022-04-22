from sheets_bd.functions.sheet import return_index_client, return_index_bank
from sheets_bd.functions.spreadsheet import Spreadsheet
from sheets_bd.models import Clients, RangeModel, SheetsResponses
from loguru import logger


def return_spreadsheet_data() -> dict:
    spreadsheet_instance = Spreadsheet('1liKyJdWvOibP5wdnrjdrbrCNhsl1AK4IEJjQSr0_csE')
    sheets_name = 'test'
    start_rows = 3
    end_rows = 1067
    column_start = 'A'
    column_end = 'CV'
    return spreadsheet_instance.reed(sheets_name, start_rows, column_start, end_rows, column_end)


def create_range_model(range_data: str) -> RangeModel:
    return RangeModel.objects.create(range_field=range_data)


def return_range_model_instance(range_data: str) -> RangeModel:
    qw = RangeModel.objects.filter(range_field=range_data)
    if qw.exists():
        return qw[0]
    return create_range_model(range_data)


def create_sheet_responses():
    spreadsheet_data = return_spreadsheet_data()
    SheetsResponses.objects.create(
        range_field=return_range_model_instance(spreadsheet_data['range']),
        response=spreadsheet_data['values'])


def return_field_client(client: list, field: str, boolean: bool = False) -> [str, bool]:
    return check_boolean_variable(client[return_index_client(field)], boolean)


def return_bank_field(client: list, field: str, bank: str, boolean: bool = False) -> [str, bool]:
    return check_boolean_variable(client[return_index_bank(bank, field)], boolean)


def check_boolean_variable(client_field: str, boolean: bool) -> [str, bool]:
    if boolean is True:
        variable_dict = {"TRUE": True, "FALSE": False}
        if client_field in variable_dict:
            return variable_dict[client_field]
        else:
            return False
    return client_field


def create_clients_model(client: list, range_data: str):
    if not Clients.objects.filter(inn=client[return_index_client("inn")]).exists():
        Clients.objects.create(
            range_field=return_range_model_instance(range_data),
            inn=return_field_client(client, "inn"), name_company=return_field_client(client, "name_company"),
            surname=return_field_client(client, "surname"), first_name=return_field_client(client, "first_name"),
            patronomic=return_field_client(client, "patronomic"), phone=return_field_client(client, "phone"),
            adress=return_field_client(client, "adress"), adress_one=return_field_client(client, "adress_one"),
            adress_two=return_field_client(client, "adress_two"), date=return_field_client(client, "date"),
            priority=return_field_client(client, "priority"),
            check_priority=return_field_client(client, "check_priority", boolean=True),
            make_general_comment=return_field_client(client, "make_general_comment"),

            alfa_status_inn=return_bank_field(client, 'status_inn', 'alfabank'),
            alfa_comment=return_bank_field(client, 'comment', 'alfabank'),
            alfa_additional_comment=return_bank_field(client, 'add_comment', 'alfabank'),
            alfa_str_comment=return_bank_field(client, 'str_comment', 'alfabank'),
            alfa_send_rko=return_bank_field(client, 'send_rko', 'alfabank', boolean=True),
            alfa_client_type=return_bank_field(client, 'client_type', 'alfabank'),
            alfa_bank_city=return_bank_field(client, 'city', 'alfabank'),
            alfa_bank_response=return_bank_field(client, 'response', 'alfabank'),
            alfa_fias=return_bank_field(client, 'fias', 'alfabank'),
            alfa_ekvairing=return_bank_field(client, 'ekvairing', 'alfabank'),
            alfa_spec_schet_44=return_bank_field(client, 'spec_schet_44', 'alfabank'),
            alfa_credit=return_bank_field(client, 'credit', 'alfabank'),

            vtb_status_inn=return_bank_field(client, 'status_inn', 'vtb'),
            vtb_comment=return_bank_field(client, 'comment', 'vtb'),
            vtb_additional_comment=return_bank_field(client, 'add_comment', 'vtb'),
            vtb_fixed=return_bank_field(client, 'to_fix', 'vtb', boolean=True),
            vtb_send=return_bank_field(client, 'send', 'vtb', boolean=True),
            vtb_client_type=return_bank_field(client, 'client_type', 'vtb'),
            vtb_bank_city=return_bank_field(client, 'city', 'vtb'),
            vtb_bank_response=return_bank_field(client, 'response', 'vtb'),
            vtb_id_application=return_bank_field(client, 'application_ID', 'vtb'),

            tinkoff_status_inn=return_bank_field(client, 'status_inn', 'tinkoff'),
            tinkoff_comment=return_bank_field(client, 'comment', 'tinkoff'),
            tinkoff_additional_comment=return_bank_field(client, 'add_comment', 'tinkoff'),
            tinkoff_send=return_bank_field(client, 'send', 'tinkoff', boolean=True),
            tinkoff_client_type=return_bank_field(client, 'client_type', 'tinkoff'),
            tinkoff_bank_city=return_bank_field(client, 'city', 'tinkoff'),
            tinkoff_bank_response=return_bank_field(client, 'response', 'tinkoff'),

            otkritie_status_inn=return_bank_field(client, 'status_inn', 'open'),
            otkritie_comment=return_bank_field(client, 'comment', 'open'),
            otkritie_additional_comment=return_bank_field(client, 'add_comment', 'open'),
            otkritie_send=return_bank_field(client, 'send', 'open', boolean=True),
            otkritie_client_type=return_bank_field(client, 'client_type', 'open'),
            otkritie_bank_city=return_bank_field(client, 'city', 'open'),
            otkritie_bank_response=return_bank_field(client, 'response', 'open'),
            otkritie_ekvaring=return_bank_field(client, 'ekvairing', 'open', boolean=True),

            tochka_status_inn=return_bank_field(client, 'status_inn', 'tochka'),
            tochka_comment=return_bank_field(client, 'comment', 'tochka'),
            tochka_additional_comment=return_bank_field(client, 'add_comment', 'tochka'),
            tochka_send=return_bank_field(client, 'send', 'tochka', boolean=True),
            tochka_client_type=return_bank_field(client, 'client_type', 'tochka'),
            tochka_bank_city=return_bank_field(client, 'city', 'tochka'),
            tochka_do_not_call=return_bank_field(client, 'dont_send', 'tochka'),
            tochka_checkbox=return_bank_field(client, 'checkbox', 'tochka'),

            psb_status_inn=return_bank_field(client, 'status_inn', 'psb'),
            psb_comment=return_bank_field(client, 'comment', 'psb'),
            psb_additional_comment=return_bank_field(client, 'add_comment', 'psb'),
            psb_send=return_bank_field(client, 'send', 'psb', boolean=True),
            psb_client_type=return_bank_field(client, 'client_type', 'psb'),
            psb_bank_city=return_bank_field(client, 'city', 'psb'),
            psb_bank_response=return_bank_field(client, 'response', 'psb'),
            psb_id_application=return_bank_field(client, 'int_field', 'psb'),

            module_comment=return_bank_field(client, 'comment', 'modul'),
            module_additional_comment=return_bank_field(client, 'add_comment', 'modul'),
            module_send=return_bank_field(client, 'send', 'modul', boolean=True),
            module_client_type=return_bank_field(client, 'client_type', 'modul'),
            module_bank_city=return_bank_field(client, 'city', 'modul'),
            module_bank_response=return_bank_field(client, 'response', 'modul'),
            module_id_application=return_bank_field(client, 'application_ID', 'modul')
        )


def start_create_clients_model():
    spreadsheet_data = return_spreadsheet_data()
    values_list = spreadsheet_data['values']
    range_data = spreadsheet_data['range']
    len_values_list = len(values_list)
    for index, client in enumerate(values_list[1:]):
        create_clients_model(client, range_data)
        logger.info(f'{index} из {len_values_list} сохранено')
