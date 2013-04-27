'''
Created on 2013-4-27

@author: EYE
'''

import json
import pprint

json_data = open("hello.json")

data = json.load(json_data)


pprint.pprint(data)

json_data.close()

