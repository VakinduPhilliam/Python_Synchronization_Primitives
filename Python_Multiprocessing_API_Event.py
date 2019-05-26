# Python Multiprocessing API
# The new multiprocessing package lets Python programs create new processes that will perform a computation and return
# a result to the parent. 
# The parent and child processes can communicate using queues and pipes, synchronize their operations using locks and semaphores,
# and can share simple arrays of data.
# The fundamental Python Multiprocessing class is the 'Process', which is passed a callable object and a collection of arguments.
# The 'start()' method sets the callable running in a subprocess, after which you can call the 'is_alive()' method to check whether
# the subprocess is still running and the 'join()' method to wait for the process to exit.
# Event
# class asyncio.Event(*, loop=None) 
# An event object. Not thread-safe.
# An asyncio event can be used to notify multiple asyncio tasks that some event has happened.
# An Event object manages an internal flag that can be set to true with the set() method and reset to false with the clear() method.
# The wait() method blocks until the flag is set to true. The flag is set to false initially.
 
async def waiter(event):
    print('waiting for it ...')
 
   await event.wait()
    print('... got it!')

async def main():

    # Create an Event object.

    event = asyncio.Event()

    # Spawn a Task to wait until 'event' is set.

    waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 1 second and set the event.

    await asyncio.sleep(1)
    event.set()

    # Wait until the waiter task is finished.

    await waiter_task

asyncio.run(main())
