from button import instantiate as make_kill_btn
from server import server_init
import threading


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

def main():
    t1_stop = threading.Event()
    t2_stop = threading.Event()
    ts = MyThread(name='server', function=server_init, args=(2, t2_stop))
    tb = MyThread(name='kill_button', function=make_kill_btn, args=(1, t1_stop))
    threads = [ts, tb]
    for proc in threads:
        proc.start()


if __name__ == '__main__':
    main()