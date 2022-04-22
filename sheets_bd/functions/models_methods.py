from google_sheets_bd.sheets_bd.functions.spreadsheet import Spreadsheet
from google_sheets_bd.sheets_bd.models import Clients


def return_spreadsheet_data():
    spreadsheet_instance = Spreadsheet('1liKyJdWvOibP5wdnrjdrbrCNhsl1AK4IEJjQSr0_csE')
    sheets_name = 'test'
    start_rows = 3
    end_rows = 1067
    column_start = 'A'
    column_end = 'CV'
    return spreadsheet_instance.reed(sheets_name, start_rows, column_start, end_rows, column_end)


def create_clients_model():
    spreadsheet_data = return_spreadsheet_data()
    range = spreadsheet_data['range']
    values_list = spreadsheet_data['values']
    print(range)
    print(values_list)
