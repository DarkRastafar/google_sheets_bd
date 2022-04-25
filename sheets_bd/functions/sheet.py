from config import BOOLEAN_VARIABLES_CLIENT_LIST, BOOLEAN_VARIABLES_BANK_LIST

tables_dict = {
    "client": {
        "inn": "A",
        "name_company": "B",
        "surname": "C",
        "first_name": "D",
        "patronomic": "E",
        "phone": "F",
        "adress": "G",
        "adress_one": "H",
        "adress_two": "I",
        "date": "J",
        "priority": "K",
        "check_priority": "L",
        "make_general_comment": "M"
    },
    "bankes": {
        "alfabank": {
            "status_inn": "N",
            "comment": "O",
            "add_comment": "P",
            "str_comment": "Q",
            "send": "R",
            "client_type": "S",
            "city": "T",
            "response": "U",
            "fias": "V",
            "ekvairing": "X",
            "spec_schet_44": "Y",
            "credit": "Z",
        },
        "vtb": {
            "status_inn": "AB",
            "comment": "AC",
            "add_comment": "AD",
            "to_fix": "AE",
            "send": "AF",
            "client_type": "AG",
            "city": "AH",
            "response": "AI",
            "application_ID": "AJ",
        },
        "open": {
            "status_inn": "BB",
            "comment": "BC",
            "add_comment": "BD",
            "send": "BE",
            "client_type": "BF",
            "city": "BG",
            "response": "BH",
            "ekvairing": "BI",
        },
        'tinkoff':
            {
            "status_inn": "AP",
            "comment": "AQ",
            "add_comment": "AR",
            "send": "AS",
            "client_type": "AT",
            "city": "AU",
            "response": "AV",
            },
        "tochka": {
            "status_inn": "BN",
            "comment": "BO",
            "add_comment": "BP",
            "send": "BQ",
            "client_type": "BR",
            "city": "BS",
            "dont_send": "BT",
            "checkbox": "BW"
        },
        "psb": {
            "status_inn": "BX",
            "comment": "BY",
            "add_comment": "BZ",
            "send": "CA",
            "client_type": "CB",
            "city": "CC",
            "response": "CD",
            "application_ID": "CE",
        },
        "module": {
            "comment": "CL",
            "add_comment": "CM",
            "send": "CN",
            "client_type": "CO",
            "city": "CP",
            "response": "CQ",
            "application_ID": "CR",
        }
    }
}



relevance_dict = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "X": 23,
    "Y": 24,
    "Z": 25,
    "AB": 27,
    "AC": 28,
    "AD": 29,
    "AE": 30,
    "AF": 31,
    "AG": 32,
    "AH": 33,
    "AI": 34,
    "AJ": 35,
    "AP": 41,
    "AQ": 42,
    "AR": 43,
    "AS": 44,
    "AT": 45,
    "AU": 46,
    "AV": 47,
    "BB": 53,
    "BC": 54,
    "BD": 55,
    "BE": 56,
    "BF": 57,
    "BG": 58,
    "BH": 59,
    "BI": 60,
    "BN": 65,
    "BO": 66,
    "BP": 67,
    "BQ": 68,
    "BR": 69,
    "BS": 70,
    "BT": 71,
    "BW": 74,
    "BX": 75,
    "BY": 76,
    "BZ": 77,
    "CA": 78,
    "CB": 79,
    "CC": 80,
    "CD": 81,
    "CE": 82,
    "CL": 89,
    "CM": 90,
    "CN": 91,
    "CO": 92,
    "CP": 93,
    "CQ": 94,
    "CR": 95

}


def return_index_client(field):
    return relevance_dict[tables_dict['client'][field]]


def return_index_bank(bank, field):
    return relevance_dict[tables_dict['bankes'][bank][field]]


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



if __name__ == "__main__":
    # print(return_index_client("inn"))
    # print(return_index_bank('alfabank', 'add_comment'))
    # create_bool_index_list()
    # print(return_bank_index_list('vtb'))
    print(return_bool_index_bank_list())
    print(return_bool_index_client_list())
