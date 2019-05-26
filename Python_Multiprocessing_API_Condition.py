# Python Multiprocessing API
# The new multiprocessing package lets Python programs create new processes that will perform a computation and return
# a result to the parent. 
# The parent and child processes can communicate using queues and pipes, synchronize their operations using locks and semaphores,
# and can share simple arrays of data.
# The fundamental Python Multiprocessing class is the 'Process', which is passed a callable object and a collection of arguments.
# The 'start()' method sets the callable running in a subprocess, after which you can call the 'is_alive()' method to check whether
# the subprocess is still running and the 'join()' method to wait for the process to exit.
# Condition
# class asyncio.Condition(lock=None, *, loop=None) 
# A Condition object. Not thread-safe.
# An asyncio condition primitive can be used by a task to wait for some event to happen and then get exclusive access to a shared resource.
# In essence, a Condition object combines the functionality of an Event and a Lock. It is possible to have multiple Condition objects share
# one Lock, which allows coordinating exclusive access to a shared resource between different tasks interested in particular states of that
# shared resource.
# The optional lock argument must be a Lock object or None. In the latter case a new Lock object is created automatically.
# The preferred way to use a Condition is an async with statement:
 
cond = asyncio.Condition()

# ... later

async with cond:
    await cond.wait()

# 
# which is equivalent to:
# 

cond = asyncio.Condition()

# ... later

await lock.acquire()

try:
    await cond.wait()

finally:
    lock.release()
