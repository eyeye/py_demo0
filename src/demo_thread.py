'''
Created on 2012-10-19

@author: EYE
'''

import time
import thread

def timer( no, interval ):
    cnt = 0
    while cnt < 10:
        print 'Thread:(%d) Time:%s\n'%(no, time.ctime())
        time.sleep(interval)
        cnt += 1
    
    thread.exit_thread()
    
    
def test():
    thread.start_new_thread(timer, (1,1))
    thread.start_new_thread(timer, (2,2))
    
    
if __name__ == '__main__':
    test()
    time.sleep(10)

