# -*- coding=UTF8 -*-

'''
Created on 2012-10-19

@author: EYE
'''

import threading
import time


class task( threading.Thread ):
    def __init__(self, num, interval):
        threading.Thread.__init__(self)
        self.num = num
        self.interval = interval
        self.req_stop = False
        
        
    def run(self):
        while not self.req_stop:
            print 'Thread Obj(%d), Time:%s\n' %(self.num, time.ctime())
            time.sleep(self.interval)
            
    def stop(self):
        self.req_stop = True
        
        
        
def test():
    thread1 = task(1, 1)
    thread2 = task(2, 2)
    
    thread1.start()
    thread2.start()
    
    time.sleep(10)
    
    thread1.stop()
    thread2.stop()

    print '测试结束'

    return





if __name__ == '__main__':
    test()



