
from lib import *
'''
1. read 함수를 한번에 DataFrame으로 가져올 수 있는 방법 찾기
     - get_as_DataFrame으로 가져온다면 Nan값을 포함함

'''
class RDlogic():

    def __init__(self, workspace):
        self.workspace = workspace


    def read(self):
        records = self.workspace.get_all_records()
        return pd.DataFrame(records)


    def writes(self):
        set_with_dataframe(self.workspace, config.configdata)
