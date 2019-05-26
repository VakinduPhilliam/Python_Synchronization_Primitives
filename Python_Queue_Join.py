# Python Queue
# queue — A synchronized queue class.
# The queue module implements multi-producer, multi-consumer queues. It is especially useful in threaded programming when
# information must be exchanged safely between multiple threads.
# The Queue class in this module implements all the required locking semantics.
# Queue.join(). 
# Blocks until all items in the queue have been gotten and processed.
# The count of unfinished tasks goes up whenever an item is added to the queue.
# The count goes down whenever a consumer thread calls task_done() to indicate that the item was retrieved and all work on it is complete.
# When the count of unfinished tasks drops to zero, join() unblocks.
# 
# Example of how to wait for enqueued tasks to be completed:
# 

def worker():

    while True:
        item = q.get()

        if item is None:
            break

        do_work(item)
        q.task_done()

q = queue.Queue()
threads = []

for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()

    threads.append(t)

for item in source():
    q.put(item)

# block until all tasks are done

q.join()

# stop workers

for i in range(num_worker_threads):
    q.put(None)

for t in threads:
    t.join()
