# Python Multiprocessing API
# The new multiprocessing package lets Python programs create new processes that will perform a computation and return
# a result to the parent. 
# The parent and child processes can communicate using queues and pipes, synchronize their operations using locks and semaphores,
# and can share simple arrays of data.
# The fundamental Python Multiprocessing class is the 'Process', which is passed a callable object and a collection of arguments.
# The 'start()' method sets the callable running in a subprocess, after which you can call the 'is_alive()' method to check whether
# the subprocess is still running and the 'join()' method to wait for the process to exit.
# The other high-level interface, the Manager class, creates a separate server process that can hold master copies of Python data structures.
# Other processes can then access and modify these data structures using proxy objects. The following example creates a shared dictionary by
# calling the dict() method; the worker processes then insert values into the dictionary. (Locking is not done for you automatically, which
# doesn’t matter in this example. Manager’s methods also include Lock(), RLock(), and Semaphore() to create shared locks.)
 

import time
from multiprocessing import Pool, Manager

def factorial(N, dictionary):
    "Compute a factorial."

    # Calculate the result

    fact = 1L
    for i in range(1, N+1):
        fact = fact * i

    # Store result in dictionary

    dictionary[N] = fact

if __name__ == '__main__':
    p = Pool(5)
    mgr = Manager()
    d = mgr.dict()         # Create shared dictionary

    # Run tasks using the pool

    for N in range(1, 1000, 10):
        p.apply_async(factorial, (N, d))

    # Mark pool as closed -- no more tasks can be added.

    p.close()

    # Wait for tasks to exit

    p.join()

    # Output results

    for k, v in sorted(d.items()):
        print k, v
