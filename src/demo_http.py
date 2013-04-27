# -*- coding=UTF8 -*-
'''
Created on 2012-10-19

@author: EYE
'''


import httplib
import demo_threading


print 'Http 测试'
conn = httplib.HTTPConnection("www.google.com")
conn.request("GET", "/")
r1 = conn.getresponse()
print r1.status, r1.reason

data1 = r1.read()
conn.request("GET", "/")
r2 = conn.getresponse()
print r2.status, r2.reason, r2.read()

data2 = r2.read()
conn.close()

demo_threading.test()



