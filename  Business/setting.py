
from config import *
'''
초기 세팅 끝내고 workspace를 return 해주는 Class 

setting 할 때 deviceinfo를 지정해주어 시트를 저장하게 함
DataLoading도 같이 역할 수행
'''

class Set:

    def __init__(self):
        self.setting_scope = scope
        self.json = json_file_name
        self.url = sheeturl
        self.credential = ServiceAccountCredentials.from_json_keyfile_name(self.json, self.setting_scope)
        self.gc = gspread.authorize((self.credential))
        self.doc = self.gc.open_by_url(self.url)
        self.sheet = '시트1' # 처리할 sheet

        self.Device()


    def Device(self):
        #json -> configjson
        pass
        #deviceinfo = json['DeviceId']

        #if deviceinfo not in sheet1device:
            #self.sheet = '시트2'



    def setsheet(self):
        return self.doc.worksheet(self.sheet)




