# -*- coding=UTF8 -*-

'''
Created on 2012-10-21

@author: EYE
'''

from serial.tools import list_ports

#com = serial.Serial();
#
#iterator = sorted()

iterator = sorted(list_ports.comports())
    # list them
for port, desc, hwid in iterator:
    print "%-20s" % (port,)
    print "    desc: %s" % (desc,)
    print "    hwid: %s" % (hwid,)
    
    
    
g = lambda x : x+2
info = [g(x) for x in range(10)] 
print info








