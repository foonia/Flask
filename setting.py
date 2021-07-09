
from config import *
'''
초기 세팅 끝내고 workspace를 return 해주는 Class 
'''

class Set:

    def __init__(self,json):
        self.setting_scope = scope
        self.json = json_file_name
        self.url = sheeturl
        self.credential = ServiceAccountCredentials.from_json_keyfile_name(self.json, self.setting_scope)
        self.gc = gspread.authorize((self.credential))
        self.doc = self.gc.open_by_url(self.url)
        self.sheet = '시트1' # 처리할 sheet

        self.setsheet()


    def Device(self,json):

        deviceinfo = json['DeviceId']

        if deviceinfo not in sheet1device:
            self.sheet = '시트2'

        return self.setsheet()

    def setsheet(self):
        print(self.sheet)
        return self.doc.worksheet(self.sheet)



