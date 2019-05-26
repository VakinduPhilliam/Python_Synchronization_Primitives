# Python _thread Module
# Low-level threading API
# This module provides low-level primitives for working with multiple threads (also called light-weight processes or tasks)
# — multiple threads of control sharing their global data space. For synchronization, simple locks (also called mutexes or
# binary semaphores) are provided. The threading module provides an easier to use and higher-level threading API built on top
# of this module.
# lock.release(): 
# Releases the lock.
# The lock must have been acquired earlier, but not necessarily by the same thread.
# lock.locked(): 
# Return the status of the lock: True if it has been acquired by some thread, False if not.
# In addition to these methods, lock objects can also be used via the with statement, e.g.:
 
import _thread

a_lock = _thread.allocate_lock()

with a_lock:
    print("a_lock is locked while this executes")
