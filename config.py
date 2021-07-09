
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

json_file_name = 'sechan-217204-eccafe3224f3.json'
sheeturl = 'https://docs.google.com/spreadsheets/d/1EcDlIlyCOTbqfP4amO4zlYkRbpQpCZyH5UWNWfqJXyM/edit#gid=0'

sheet1device = ['D5001','D5002']

#test 2 url : https://docs.google.com/spreadsheets/d/1EcDlIlyCOTbqfP4amO4zlYkRbpQpCZyH5UWNWfqJXyM/edit#gid=0
#test 1 url : https://docs.google.com/spreadsheets/d/1o7jy-yjZ-gspw6_SW4jbxxPdOywlFE49GGV4v06aja0/edit#gid=0


