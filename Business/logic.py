import sys,os
sys.path.append(os.path.dirname(os.path.abspath((os.path.dirname(__file__)))))
from globalpackage import lib
from globalpackage import config

class Logic:

    def __init__(self):


        self.idx = self.checkInfromMAC()

    def checkInfromMAC(self):

        if config.configjson['MAC 주소'] in list(config.configdata['MAC 주소']):
            return list(config.configdata['MAC 주소']).index

        return -1

    def update(self):

        for id,v in enumerate(config.configjson.values):
            config.configdata[self.idx][id] = v

    def append(self):
        config.configdata = config.configdata.append(config.configjson,ignore_index = True)




