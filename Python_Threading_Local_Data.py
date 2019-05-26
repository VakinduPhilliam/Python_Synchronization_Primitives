# Python Threading
# threading — Thread-based parallelism
# This module constructs higher-level threading interfaces on top of the lower level _thread module. 
# Thread-Local Data. 
# Thread-local data is data whose values are thread specific. To manage thread-local data, just create
# an instance of local (or a subclass) and store attributes on it:
 
mydata = threading.local()
mydata.x = 1
