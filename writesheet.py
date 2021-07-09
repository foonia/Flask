
from lib import *

class Wirte():

    def __init__(self, data):
        self.data = data

    def write(self,workspace):
        set_with_dataframe(workspace, self.data)
