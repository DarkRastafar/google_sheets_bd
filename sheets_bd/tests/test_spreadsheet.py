from unittest import TestCase
import sys
import googleapiclient
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

from google_sheets_bd.sheets_bd.functions.spreadsheet import Spreadsheet
from threading import Thread

sys.path.append('C:\\bd_for_google_sheets\\')
from config import CREDENTIALS_FILE


class SpreadsheetTestCase(TestCase):
    def setUp(self):
        self.spreadsheet_id = '1liKyJdWvOibP5wdnrjdrbrCNhsl1AK4IEJjQSr0_csE'
        self.obj = Spreadsheet(self.spreadsheet_id)

    def test_reed(self):
        sheets_name = 'test'
        start_rows = 3
        end_rows = 1067
        column_start = 'A'
        column_end = 'CV'
        test_res = self.obj.reed(sheets_name, start_rows, column_start, end_rows, column_end)
        print(test_res['range'])
        print(test_res['values'])

    def test_write(self):
        data = [{'values': [['hjkj']], 'range': 'test!T6', 'majorDimension': 'ROWS'},
                {'values': [['hjkj']], 'range': 'test!T7', 'majorDimension': 'ROWS'}]
        print(self.obj.write(data))

    def test_append(self):
        list_name = 'test'
        list_google = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Барнаул']]
        print(self.obj.append(list_name, list_google))

    def test_update(self):
        body = {
            "requests":
                [{"repeatCell":
                      {"cell":
                           {"userEnteredFormat": {}}, "range":
                           {
                               "sheetId": '2078580582',
                               "startRowIndex": 5,
                               "endRowIndex": 8,
                               "startColumnIndex": 1,
                               "endColumnIndex": 4
                           },
                       "fields": "userEnteredFormat"}}]}
        print(self.obj.update(body))

    def test_test(self):
        def servise_():
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                   'https://www.googleapis.com/auth/drive'])

            httpAuth = credentials.authorize(httplib2.Http())
            service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
            return service

        def write():
            servise = servise_()
            servise.spreadsheets().values().batchUpdate(
                spreadsheetId='1liKyJdWvOibP5wdnrjdrbrCNhsl1AK4IEJjQSr0_csE',
                body={"valueInputOption": "USER_ENTERED",
                      "data": [{'values': [['hjkj']], 'range': 'test!T6', 'majorDimension': 'ROWS'},
                               {'values': [['hjkj']], 'range': 'test!T7', 'majorDimension': 'ROWS'}]}).execute()
            servise.close()

        lisr_tread = []

        for i in range(20):
            lisr_tread.append(Thread(target=write))

        for tread in lisr_tread:
            tread.start()

        for thread in lisr_tread:
            thread.join()
