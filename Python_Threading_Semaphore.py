# Python Threading
# threading � Thread-based parallelism
# This module constructs higher-level threading interfaces on top of the lower level _thread module. 
#
# Semaphore.
# Semaphores are often used to guard resources with limited capacity, for example, a database server.
# In any situation where the size of the resource is fixed, you should use a bounded semaphore.
# Before spawning any worker threads, your main thread would initialize the semaphore:
# 

maxconnections = 5

# ...

pool_sema = BoundedSemaphore(value=maxconnections)
 
#
# Once spawned, worker threads call the semaphore�s acquire and release methods when they need to connect
# to the server:
# 

with pool_sema:
    conn = connectdb()

    try:

        # ... use connection ...

    finally:
        conn.close()
 
#
# The use of a bounded semaphore reduces the chance that a programming error which causes the semaphore to be
# released more than it�s acquired will go undetected.
#