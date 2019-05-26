# Python Threading
# threading — Thread-based parallelism
# This module constructs higher-level threading interfaces on top of the lower level _thread module. 
#
# wait_for(predicate, timeout=None) 
# Wait until a condition evaluates to true. predicate should be a callable which result will be interpreted
# as a boolean value.
# A timeout may be provided giving the maximum time to wait.
# This utility method may call wait() repeatedly until the predicate is satisfied, or until a timeout occurs.
# The return value is the last return value of the predicate and will evaluate to False if the method timed out.
# Ignoring the timeout feature, calling this method is roughly equivalent to writing:
 
while not predicate():
    cv.wait()
