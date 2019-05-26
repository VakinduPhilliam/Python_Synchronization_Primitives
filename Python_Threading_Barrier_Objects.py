# Python Threading
# threading — Thread-based parallelism
# This module constructs higher-level threading interfaces on top of the lower level _thread module. 
#
# Barrier Objects.
# 
# This class provides a simple synchronization primitive for use by a fixed number of threads that need
# to wait for each other.
# Each of the threads tries to pass the barrier by calling the wait() method and will block until all of
# the threads have made their wait() calls.
# At this point, the threads are released simultaneously.
# 
# The barrier can be reused any number of times for the same number of threads.
# 
# As an example, here is a simple way to synchronize a client and server thread:
# 

b = Barrier(2, timeout=5)

def server():
    start_server()
    b.wait()

    while True:
        connection = accept_connection()
        process_server_connection(connection)

def client():
    b.wait()

    while True:
        connection = make_connection()

        process_client_connection(connection)
