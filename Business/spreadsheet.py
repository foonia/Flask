import sys,os
sys.path.append(os.path.dirname(os.path.abspath((os.path.dirname(__file__)))))
from globalpackage import lib
from dataflow import *

u = updateData()
u.runupdate()

