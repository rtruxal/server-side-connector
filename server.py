import socket


def server_init():
    sock = socket.socket()
    host = socket.gethostname()
    port = 12345
    sock.bind((host, port))

    sock.listen(5)
    while True:
        c, addr = sock.accept()
        print 'Got connection from {}'.format(addr)
        c.send('Thanks for connecting! Now peace.')
        c.close()

