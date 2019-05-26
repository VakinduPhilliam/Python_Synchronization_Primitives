# Python Multiprocessing API
# The new multiprocessing package lets Python programs create new processes that will perform a computation and return
# a result to the parent. 
# The parent and child processes can communicate using queues and pipes, synchronize their operations using locks and semaphores,
# and can share simple arrays of data.
# The fundamental Python Multiprocessing class is the 'Process', which is passed a callable object and a collection of arguments.
# The 'start()' method sets the callable running in a subprocess, after which you can call the 'is_alive()' method to check whether
# the subprocess is still running and the 'join()' method to wait for the process to exit.
# A Queue is used to communicate the result of the factorial.
# The Queue object is stored in a global variable.
# The child process will use the value of the variable when the child was created; because it’s a Queue, parent and child can use the
# object to communicate. (If the parent were to change the value of the global variable, the child’s value would be unaffected, and vice versa.)
# This simple subprocess will calculate a factorial. 
# The function doing the calculation is written strangely so that it takes significantly longer when the input argument is a multiple
# of 4.
 

import time
from multiprocessing import Process, Queue

def factorial(queue, N):
    "Compute a factorial."

    # If N is a multiple of 4, this function will take much longer.

    if (N % 4) == 0:
        time.sleep(.05 * N/4)

    # Calculate the result

    fact = 1L
    for i in range(1, N+1):
        fact = fact * i

    # Put the result on the queue

    queue.put(fact)

if __name__ == '__main__':
    queue = Queue()

    N = 5

    p = Process(target=factorial, args=(queue, N))
    p.start()
    p.join()

    result = queue.get()

    print 'Factorial', N, '=', result
