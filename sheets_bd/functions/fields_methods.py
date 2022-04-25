from config import BANK_LIST, EXCEPTION_LIST, BOOLEAN_VARIABLES_CLIENT_LIST, MAX_LEN_CLIENT
from sheets_bd.functions.sheet import return_index_client, return_index_bank, return_bool_index_bank_list, \
    return_bool_index_client_list
from sheets_bd.models import Clients


def check_field(field: str) -> bool:
    for bank in BANK_LIST:
        if field.startswith(bank):
            return False
    else:
        return True


def return_model_fields(bank: str = None) -> list:
    if bank is None:
        return [field.name for field in Clients._meta.get_fields()
                if (check_field(field.name) is True) and (field.name not in EXCEPTION_LIST)]
    elif bank in BANK_LIST:
        return [field.name for field in Clients._meta.get_fields() if bank in field.name]


def return_field_client(client: list, field: str, boolean: bool = False) -> [str, bool]:
    try:
        return check_boolean_variable(client[return_index_client(field)], boolean)
    except:
        if boolean is not None:
            return boolean
        return ''


def return_bank_field(client: list, field: str, bank: str, boolean: bool = False) -> [str, bool]:
    try:
        return check_boolean_variable(client[return_index_bank(bank, field)], boolean)
    except:
        if boolean is True:
            return boolean
        return ''


def check_boolean_variable(client_field: str, boolean: bool) -> [str, bool]:
    if boolean is True:
        variable_dict = {"TRUE": True, "FALSE": False}
        if client_field in variable_dict:
            return variable_dict[client_field]
        else:
            return False
    return client_field


def create_kwargs_client(client: list, bank: str = None) -> dict:
    kwargs_client = {}
    for field in return_model_fields(bank):
        kwargs_client.update({field: return_field_client(client, field)})
    return kwargs_client


def extend_client_indexes(client: list) -> None:
    len_client = len(client)
    if len_client < MAX_LEN_CLIENT:
        for index in range(len_client, MAX_LEN_CLIENT + 1):
            client.insert(index, '')


def boolean_mutation(client: list) -> None:
    bool_indexes = return_bool_index_client_list() + return_bool_index_bank_list()
    for index, var in enumerate(client):
        if index in bool_indexes:
            client[index] = bool(client[index]) if client[index] == ('TRUE' or 'FALSE') else False


def mutation_inn(client: list) -> str:
    if len(client[0]) == 11 or len(client[0]) == 9:
        client[0] = f'0{client[0]}'
    client[0] = client[0].replace('.0', '')
    if len(client[0]) == 10 or len(client[0]) == 12:
        return client[0]
    return client[0]


def return_mutation_client(client: list) -> list:
    for func in [extend_client_indexes, boolean_mutation, mutation_inn]:
        func(client)
    return client

