# Python Threading
# threading — Thread-based parallelism
# This module constructs higher-level threading interfaces on top of the lower level _thread module. 
#
# Timer Objects.
# 
# This class represents an action that should be run only after a certain amount of time has passed — a timer.
# Timer is a subclass of Thread and as such also functions as an example of creating custom threads.
# 
# Timers are started, as with threads, by calling their start() method. The timer can be stopped (before its action
# has begun) by calling the cancel() method. The interval the timer will wait before executing its action may not be
# exactly the same as the interval specified by the user.
# 
# For example:
# 

def hello():
    print("hello, world")

t = Timer(30.0, hello)

t.start()  # after 30 seconds, "hello, world" will be printed
