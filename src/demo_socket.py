# -*- coding=UTF8 -*-

'''
Created on 2012-10-20

@author: EYE
'''


import threading
import socket

class Server( threading.Thread ):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.req_stop = False
        
    def run(self):
        
        self.sock.bind(('localhost', 20000))
        self.sock.listen(5)
        conn, addr = self.sock.accept()
        print 'connected :', addr
        
        while not self.req_stop:
            
            try:
                buf = conn.recv(64)
                print 'server echo: ', buf
                
                if buf == 'quit':
                    print '服务端退出'
                    conn.close()
                    self.req_stop = True
                    
            except socket.timeout:
                print 'server timeout'
                conn.close()
        
        
        
class Client( threading.Thread ):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.req_stop = False
        
        
    def run(self):
        
        self.sock.connect(('localhost', 20000))
        
        while not self.req_stop:
            buf_send = raw_input("\n发送到服务端：")
            self.sock.send(buf_send)
            
            if buf_send == 'quit':
                print '客户端退出'
                self.req_stop = True
                
        self.sock.close()
        
           
        
def test():
    svr = Server()
    clt = Client()
    
    svr.start()
    clt.start()
    
    svr.join();
    clt.join();
    
    print '运行结束！！！'

    return





if __name__ == '__main__':
    test()



