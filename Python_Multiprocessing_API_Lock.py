# Python Multiprocessing API
# The new multiprocessing package lets Python programs create new processes that will perform a computation and return
# a result to the parent. 
# The parent and child processes can communicate using queues and pipes, synchronize their operations using locks and semaphores,
# and can share simple arrays of data.
# The fundamental Python Multiprocessing class is the 'Process', which is passed a callable object and a collection of arguments.
# The 'start()' method sets the callable running in a subprocess, after which you can call the 'is_alive()' method to check whether
# the subprocess is still running and the 'join()' method to wait for the process to exit.
# Lock
# class asyncio.Lock(*, loop=None) 
# Implements a mutex lock for asyncio tasks. Not thread-safe.
# An asyncio lock can be used to guarantee exclusive access to a shared resource.
 
# The preferred way to use a Lock is an async with statement:
 
lock = asyncio.Lock()

# ... later

async with lock:

    # access shared state
 
#
# which is equivalent to:
# 

lock = asyncio.Lock()

# ... later

await lock.acquire()

try:
    # access shared state

finally:
    lock.release()
