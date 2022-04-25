import time
from config import BANK_LIST
from sheets_bd.functions.fields_methods import (create_kwargs_client, return_mutation_client, create_kwargs_banks)
from sheets_bd.functions.spreadsheet import Spreadsheet
from sheets_bd.models import Clients, RangeModel, SheetsResponses
from loguru import logger


start_rows = 3


def return_spreadsheet_data() -> dict:
    spreadsheet_instance = Spreadsheet('1liKyJdWvOibP5wdnrjdrbrCNhsl1AK4IEJjQSr0_csE')
    sheets_name = 'test'
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


def create_clients_model(index: int, client: list, range_data: str) -> None:
    kwargs_client = create_kwargs_client(client)
    kwards_banks = create_kwargs_banks(client, BANK_LIST)
    Clients.objects.create(
        range_field=return_range_model_instance(range_data),
        diapason_row=index + start_rows,
        **kwargs_client,
        **kwards_banks
    )


def start_create_clients_model() -> None:
    spreadsheet_data = return_spreadsheet_data()
    values_list = spreadsheet_data['values']
    range_data = spreadsheet_data['range']
    len_values_list = len(values_list)
    start = time.monotonic()
    for index, client in enumerate(values_list[1:]):
        client = return_mutation_client(client)
        create_clients_model(index, client, range_data)
        logger.info(f'{index} из {len_values_list} сохранено')
    print(f'end time ---> {time.monotonic() - start}')
