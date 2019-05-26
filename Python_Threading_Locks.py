# Python Threading
# threading — Thread-based parallelism
# This module constructs higher-level threading interfaces on top of the lower level _thread module. 
#
# Using locks, conditions, and semaphores in the with statement.
# 
# All of the objects provided by this module that have acquire() and release() methods can be used as
# context managers for a with statement.
# The acquire() method will be called when the block is entered, and release() will be called when the
# block is exited.
#
# Hence:
# 

with some_lock:

    # do something...
 
#
#
# is equivalent to:
#
# 

some_lock.acquire()

try:
    # do something...

finally:
    some_lock.release()
