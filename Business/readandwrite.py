import sys,os
sys.path.append(os.path.dirname(os.path.abspath((os.path.dirname(__file__)))))
from globalpackage import lib
from globalpackage import config
'''
1. read 함수를 한번에 DataFrame으로 가져올 수 있는 방법 찾기
     - get_as_DataFrame으로 가져온다면 Nan값을 포함함

'''
class RDlogic():

    def __init__(self, workspace):
        self.workspace = workspace


    def read(self):
        records = self.workspace.get_all_records()
        return lib.pd.DataFrame(records)


    def writes(self):
        lib.set_with_dataframe(self.workspace, config.configdata)
