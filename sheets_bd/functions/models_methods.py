import time
from sheets_bd.functions.fields_methods import create_kwargs_client, return_bank_field
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


def create_sheet_responses() -> None:
    spreadsheet_data = return_spreadsheet_data()
    SheetsResponses.objects.create(
        range_field=return_range_model_instance(spreadsheet_data['range']),
        response=spreadsheet_data['values'])


def create_clients_model(client: list, range_data: str) -> None:
    kwargs_client = create_kwargs_client(client)
    Clients.objects.create(
        range_field=return_range_model_instance(range_data),
        # inn=return_field_client(client, "inn"),
        # name_company=return_field_client(client, "name_company"),
        # surname=return_field_client(client, "surname"), first_name=return_field_client(client, "first_name"),
        # patronomic=return_field_client(client, "patronomic"), phone=return_field_client(client, "phone"),
        # adress=return_field_client(client, "adress"), adress_one=return_field_client(client, "adress_one"),
        # adress_two=return_field_client(client, "adress_two"), date=return_field_client(client, "date"),
        # priority=return_field_client(client, "priority"),
        # check_priority=return_field_client(client, "check_priority", boolean=True),
        # make_general_comment=return_field_client(client, "make_general_comment"),
        **kwargs_client,
        alfa_status_inn=return_bank_field(client, 'status_inn', 'alfabank'),
        alfa_comment=return_bank_field(client, 'comment', 'alfabank'),
        alfa_add_comment=return_bank_field(client, 'add_comment', 'alfabank'),
        alfa_str_comment=return_bank_field(client, 'str_comment', 'alfabank'),
        alfa_send=return_bank_field(client, 'send', 'alfabank', boolean=True),
        alfa_client_type=return_bank_field(client, 'client_type', 'alfabank'),
        alfa_city=return_bank_field(client, 'city', 'alfabank'),
        alfa_response=return_bank_field(client, 'response', 'alfabank'),
        alfa_fias=return_bank_field(client, 'fias', 'alfabank'),
        alfa_ekvairing=return_bank_field(client, 'ekvairing', 'alfabank'),
        alfa_spec_schet_44=return_bank_field(client, 'spec_schet_44', 'alfabank'),
        alfa_credit=return_bank_field(client, 'credit', 'alfabank'),

        vtb_status_inn=return_bank_field(client, 'status_inn', 'vtb'),
        vtb_comment=return_bank_field(client, 'comment', 'vtb'),
        vtb_add_comment=return_bank_field(client, 'add_comment', 'vtb'),
        vtb_to_fix=return_bank_field(client, 'to_fix', 'vtb', boolean=True),
        vtb_send=return_bank_field(client, 'send', 'vtb', boolean=True),
        vtb_client_type=return_bank_field(client, 'client_type', 'vtb'),
        vtb_city=return_bank_field(client, 'city', 'vtb'),
        vtb_response=return_bank_field(client, 'response', 'vtb'),
        vtb_application_ID=return_bank_field(client, 'application_ID', 'vtb'),

        tinkoff_status_inn=return_bank_field(client, 'status_inn', 'tinkoff'),
        tinkoff_comment=return_bank_field(client, 'comment', 'tinkoff'),
        tinkoff_add_comment=return_bank_field(client, 'add_comment', 'tinkoff'),
        tinkoff_send=return_bank_field(client, 'send', 'tinkoff', boolean=True),
        tinkoff_client_type=return_bank_field(client, 'client_type', 'tinkoff'),
        tinkoff_city=return_bank_field(client, 'city', 'tinkoff'),
        tinkoff_response=return_bank_field(client, 'response', 'tinkoff'),

        otkritie_status_inn=return_bank_field(client, 'status_inn', 'open'),
        otkritie_comment=return_bank_field(client, 'comment', 'open'),
        otkritie_add_comment=return_bank_field(client, 'add_comment', 'open'),
        otkritie_send=return_bank_field(client, 'send', 'open', boolean=True),
        otkritie_client_type=return_bank_field(client, 'client_type', 'open'),
        otkritie_city=return_bank_field(client, 'city', 'open'),
        otkritie_response=return_bank_field(client, 'response', 'open'),
        otkritie_ekvaring=return_bank_field(client, 'ekvairing', 'open', boolean=True),

        tochka_status_inn=return_bank_field(client, 'status_inn', 'tochka'),
        tochka_comment=return_bank_field(client, 'comment', 'tochka'),
        tochka_add_comment=return_bank_field(client, 'add_comment', 'tochka'),
        tochka_send=return_bank_field(client, 'send', 'tochka', boolean=True),
        tochka_client_type=return_bank_field(client, 'client_type', 'tochka'),
        tochka_city=return_bank_field(client, 'city', 'tochka'),
        tochka_dont_send=return_bank_field(client, 'dont_send', 'tochka'),
        tochka_checkbox=return_bank_field(client, 'checkbox', 'tochka'),

        psb_status_inn=return_bank_field(client, 'status_inn', 'psb'),
        psb_comment=return_bank_field(client, 'comment', 'psb'),
        psb_add_comment=return_bank_field(client, 'add_comment', 'psb'),
        psb_send=return_bank_field(client, 'send', 'psb', boolean=True),
        psb_client_type=return_bank_field(client, 'client_type', 'psb'),
        psb_city=return_bank_field(client, 'city', 'psb'),
        psb_response=return_bank_field(client, 'response', 'psb'),
        psb_application_ID=return_bank_field(client, 'application_ID', 'psb'),

        module_comment=return_bank_field(client, 'comment', 'modul'),
        module_add_comment=return_bank_field(client, 'add_comment', 'modul'),
        module_send=return_bank_field(client, 'send', 'modul', boolean=True),
        module_client_type=return_bank_field(client, 'client_type', 'modul'),
        module_city=return_bank_field(client, 'city', 'modul'),
        module_response=return_bank_field(client, 'response', 'modul'),
        module_application_ID=return_bank_field(client, 'application_ID', 'modul')
    )


def start_create_clients_model() -> None:
    spreadsheet_data = return_spreadsheet_data()
    values_list = spreadsheet_data['values']
    range_data = spreadsheet_data['range']
    len_values_list = len(values_list)
    start = time.monotonic()
    for index, client in enumerate(values_list[1:]):
        create_clients_model(client, range_data)
        logger.info(f'{index} из {len_values_list} сохранено')
    print(f'end time ---> {time.monotonic() - start}')
