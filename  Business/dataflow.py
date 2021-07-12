from lib import *

class updateData():

    def __init__(self):
        pass

    def runupdate(self):

        runset = Set()
        workspace = runset.setsheet()

        RD = RDlogic(workspace)
        config.configdata = RD.read()

        flow = Logic()

        flow.append()

        RD.writes()