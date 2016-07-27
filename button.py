#import socket
#import threading
from kivy.app import App
from kivy.uix.button import Button




class Butt(Button):
    def __init__(self, *args, **kwargs):
        super(Butt, self).__init__(**kwargs)

    def when_pressed(self, *args):
        print 'YOU KILLLLLLEDDDD ITTTTTTT'


# class Server(object):
#     def __init__(self, port_num=8080):
#         self.port = port_num
#
#     def run(self):
#         self.sock = socket.socket()
#         self.host = socket.gethostname()
#         self.sock.bind((self.host, self.port))
#
#         self.sock.listen(5)
#         while True:
#             c, addr = self.sock.accept()
#             print 'Got connection from {}'.format(addr)
#             c.send('Thanks for connecting! Now peace.')
#             c.close()

class ServerWButtonApp(App):

    def build(self):
        butt = Butt(text='Shutdown Server')
        butt.bind(on_press=butt.when_pressed)
        #serv = Server(port_num=12345)
        return butt


def instantiate():
    ServerWButtonApp().run()

if __name__ == '__main__':
    ServerWButtonApp().run()