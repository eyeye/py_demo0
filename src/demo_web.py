# -*- coding=UTF8 -*-

'''
Created on 2012-10-21

@author: EYE
'''

import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()



