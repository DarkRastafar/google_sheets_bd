import sys
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

sys.path.append('C:\\google_sheets_bd\\')
from config import CREDENTIALS_FILE


class SpreadsheetABS:
    def __init__(self):
        pass


class Spreadsheet(SpreadsheetABS):
    def __init__(self, spreadsheet_id):
        super().__init__()
        self.spreadsheet_id = spreadsheet_id
        self.service = self.avtorization()

    def avtorization(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
        return service

    def reed(self, sheets_name, start_rows, column_start, end_rows, column_end):
        if end_rows == None:
            end_rows = ''
        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=f'{sheets_name}!{column_start}{start_rows}:{column_end}{end_rows}',
            majorDimension='ROWS'
        ).execute()
        return values

    def write(self, data):
        self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": data
            }

        ).execute()

    def append(self, list_name, list_google):
        self.service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id,
            range=f"{list_name}",
            valueInputOption='USER_ENTERED',
            insertDataOption='INSERT_ROWS',
            body={"majorDimension": 'ROWS',
                  "values": list_google}).execute()

    def update(self, body):
        results = self.service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body=body).execute()
        return results
