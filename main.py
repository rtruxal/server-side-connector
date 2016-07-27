from server import server_init
import threading
from kivy.app import App
from kivy.uix.button import Button


class MyThread(threading.Thread):
    def __init__(self, function, *args, **kwargs):
        self.running = False
        self.function = function
        super(MyThread, self).__init__(*args, **kwargs)

    def start(self):
        self.running = True
        super(MyThread, self).start()

    def run(self):
        while self.running:
            self.function()

    def stop(self):
        self.running = False


class Butt(Button):
    def __init__(self, *args, **kwargs):
        super(Butt, self).__init__(**kwargs)

    def when_pressed(self, *args):
        print 'YOU KILLLLLLEDDDD ITTTTTTT'
        print event.is_set()
        event.set()
        print event.is_set()

class ServerWButtonApp(App):

    def build(self):
        butt = Butt(text='Shutdown Server')
        butt.bind(on_press=butt.when_pressed)
        #serv = Server(port_num=12345)
        return butt


def instantiate():
    ServerWButtonApp().run()

## LOOK AT THE THREAD ARGUMENTS TO SEE HOWTF YOU PASS AN EVENT FLAG PROPERLY.
event = threading.Event()
ts = MyThread(name='server', function=server_init, args=(1, event))
tb = MyThread(name='kill_button', function=instantiate, args=(2, event))
threads = [ts, tb]
for proc in threads:
    proc.start()