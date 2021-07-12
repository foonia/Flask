
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

json_file_name = None
sheeturl = 'https://docs.google.com/spreadsheets/d/1EcDlIlyCOTbqfP4amO4zlYkRbpQpCZyH5UWNWfqJXyM/edit#gid=0'

sheet1device = ['D5001','D5002']

configdata = None
configjson ={
    '단말': '기가지니5',
    'MAC 주소': '1234',
    'SAID' : 'T13',
    'OTV 개통여부' : 'O',
    '사용자': '최세찬',
}

#test 2 url : https://docs.google.com/spreadsheets/d/1EcDlIlyCOTbqfP4amO4zlYkRbpQpCZyH5UWNWfqJXyM/edit#gid=0
#test 1 url : https://docs.google.com/spreadsheets/d/1o7jy-yjZ-gspw6_SW4jbxxPdOywlFE49GGV4v06aja0/edit#gid=0


