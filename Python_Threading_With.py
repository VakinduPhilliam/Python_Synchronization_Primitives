# Python Threading
# threading — Thread-based parallelism
# This module constructs higher-level threading interfaces on top of the lower level _thread module. 
# The typical programming style using condition variables uses the lock to synchronize access to some shared state; threads
# that are interested in a particular change of state call wait() repeatedly until they see the desired state, while threads
# that modify the state call notify() or notify_all() when they change the state in such a way that it could possibly be a desired
# state for one of the waiters. For example, the following code is a generic producer-consumer situation with unlimited buffer
# capacity:
# 
# Consume one item
#

with cv:
    while not an_item_is_available():

        cv.wait()
    get_an_available_item()

# Produce one item

with cv:
    make_an_item_available()

    cv.notify()

