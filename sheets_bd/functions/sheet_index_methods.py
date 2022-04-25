import sys

sys.path.append('C:\\CustomMethods\\custom_Spreadsheet\\')

from sheet import relevance_dict, tables_dict, return_index_client, return_index_bank
from config import (BOOLEAN_VARIABLES_CLIENT_LIST, BOOLEAN_VARIABLES_BANK_LIST, BANK_LIST, EXCEPTION_LIST,
                    MAX_LEN_CLIENT)


def return_bank_index_list(bank):
    return [relevance_dict[tables_dict['bankes'][bank][bool_field]]
            for bool_field in BOOLEAN_VARIABLES_BANK_LIST
            if bool_field in tables_dict['bankes'][bank]]


def return_bool_index_bank_list():
    result = []
    for bank in tables_dict['bankes']:
        result.extend(return_bank_index_list(bank))
    return result


def return_bool_index_client_list():
    return [relevance_dict[tables_dict['client'][bool_field]]
            for bool_field in BOOLEAN_VARIABLES_CLIENT_LIST
            if bool_field in tables_dict['client']]
