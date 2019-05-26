# Python selectors — High-level I/O multiplexing
# This module allows high-level and efficient I/O multiplexing, built upon the select module primitives.
# Users are encouraged to use this module instead, unless they want precise control over the OS-level primitives used.
# It defines a BaseSelector abstract base class, along with several concrete implementations (KqueueSelector, EpollSelector…),
# that can be used to wait for I/O readiness notification on multiple file objects. In the following, “file object” refers to
# any object with a fileno() method, or a raw file descriptor.
# A simple echo server implementation:
 
import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready

    print('accepted', conn, 'from', addr)

    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready

    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block

    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 1234))

sock.listen(100)
sock.setblocking(False)

sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()

    for key, mask in events:
        callback = key.data

        callback(key.fileobj, mask)
