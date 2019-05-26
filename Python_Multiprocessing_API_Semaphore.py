# Python Multiprocessing API
# The new multiprocessing package lets Python programs create new processes that will perform a computation and return
# a result to the parent. 
# The parent and child processes can communicate using queues and pipes, synchronize their operations using locks and semaphores,
# and can share simple arrays of data.
# The fundamental Python Multiprocessing class is the 'Process', which is passed a callable object and a collection of arguments.
# The 'start()' method sets the callable running in a subprocess, after which you can call the 'is_alive()' method to check whether
# the subprocess is still running and the 'join()' method to wait for the process to exit.
# Semaphore
# class asyncio.Semaphore(value=1, *, loop=None) 
# A Semaphore object. Not thread-safe.
# A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release() call.
# The counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting until some task calls release().
# The optional value argument gives the initial value for the internal counter (1 by default). If the given value is less than 0 a
# ValueError is raised.
# The preferred way to use a Semaphore is an async with statement:
 
sem = asyncio.Semaphore(10)

# ... later

async with sem:

    # work with shared resource
 
# 
# which is equivalent to:
# 

sem = asyncio.Semaphore(10)

# ... later

await sem.acquire()

try:

    # work with shared resource

finally:
    sem.release()
