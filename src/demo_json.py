'''
Created on 2013-4-27

@author: EYE
'''

import json
import pprint
from jinja2 import Template



json_data = open("hello.json", 'r')
temp_data = open("templates/hello.ctemp", 'r')
c_file = open("template.c", 'w')


template = Template(temp_data.read())

data = json.load(json_data)

c_file.write(template.render(ble=data))

pprint.pprint(c_file)

json_data.close()
c_file.close();
