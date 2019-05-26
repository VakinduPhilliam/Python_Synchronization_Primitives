# Python Threading
# threading — Thread-based parallelism
# This module constructs higher-level threading interfaces on top of the lower level _thread module. 
# The 'while' loop checking for the application’s condition is necessary because wait() can return after
# an arbitrary long time, and the condition which prompted the notify() call may no longer hold true.
# This is inherent to multi-threaded programming. The wait_for() method can be used to automate the condition
# checking, and eases the computation of timeouts:
# 
# Consume an item
#

with cv:
    cv.wait_for(an_item_is_available)

    get_an_available_item()

# 
# To choose between notify() and notify_all(), consider whether one state change can be interesting for only one
# or several waiting threads. E.g. in a typical producer-consumer situation, adding one item to the buffer only
# needs to wake up one consumer thread.
#