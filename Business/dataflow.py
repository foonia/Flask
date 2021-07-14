import sys,os
sys.path.append(os.path.dirname(os.path.abspath((os.path.dirname(__file__)))))
from globalpackage import lib
from globalpackage import config

class updateData():

    def __init__(self):
        pass

    def runupdate(self):

        runset = lib.setting.Set()
        workspace = runset.setsheet()

        RD = lib.readandwrite.RDlogic(workspace)
        config.configdata = RD.read()
        flow = lib.logic.Logic()

        flow.append()

        RD.writes()