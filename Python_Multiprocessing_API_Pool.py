# Python Multiprocessing API
# The new multiprocessing package lets Python programs create new processes that will perform a computation and return
# a result to the parent. 
# The parent and child processes can communicate using queues and pipes, synchronize their operations using locks and semaphores,
# and can share simple arrays of data.
# The fundamental Python Multiprocessing class is the 'Process', which is passed a callable object and a collection of arguments.
# The 'start()' method sets the callable running in a subprocess, after which you can call the 'is_alive()' method to check whether
# the subprocess is still running and the 'join()' method to wait for the process to exit.
# Two other classes, Pool and Manager, provide higher-level interfaces. 
# Pool will create a fixed number of worker processes, and requests can then be distributed to the workers by calling apply() or apply_async()
# to add a single request, and map() or map_async() to add a number of requests.
# The following code uses a Pool to spread requests across 5 worker processes and retrieve a list of results:
 
from multiprocessing import Pool

def factorial(N, dictionary):
    "Compute a factorial."

#    ...

p = Pool(5)
result = p.map(factorial, range(1, 1000, 10))

for v in result:
    print v
