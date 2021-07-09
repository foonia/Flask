import setting
from gspread_dataframe import set_with_dataframe
import pandas as pd
from testjosn import *
import gspread as gd


workspace = setting.Set(json_info)

print(workspace)
'''
def get_dataframe():
    colums = ['단말','MAC 주소','SAID', 'OTV 개통여부', '사용자', '시리얼포트', '비고']
    data = workspace.get_all_values()[1:]

    return pd.DataFrame(data, columns=colums)

def checkindata():

    data = get_dataframe()
    if info2['MAC 주소'] in list(data['MAC 주소']):
        return list(data['MAC 주소']).index(info2['MAC 주소'])

    else:
         return -1

idx = checkindata()

if idx ==-1:
    print('append')
else:
    print('replace code')
data = get_dataframe()

for id, v in enumerate(info2.values()):
    data.loc[idx][id] = v



set_with_dataframe(workspace,data)
'''