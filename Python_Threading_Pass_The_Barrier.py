# Python Threading
# threading — Thread-based parallelism
# This module constructs higher-level threading interfaces on top of the lower level _thread module. 
# class threading.Barrier(parties, action=None, timeout=None). 
# Create a barrier object for parties number of threads. An action, when provided, is a callable to be
# called by one of the threads when they are released.
# 'timeout' is the default timeout value if none is specified for the wait() method.
# wait(timeout=None). 
# Pass the barrier.
# When all the threads party to the barrier have called this function, they are all released simultaneously.
# If a timeout is provided, it is used in preference to any that was supplied to the class constructor.
# 
# The return value is an integer in the range 0 to parties – 1, different for each thread.
# This can be used to select a thread to do some special housekeeping, e.g.:
 
i = barrier.wait()

if i == 0:

    # Only one thread needs to print this

    print("passed the barrier")
