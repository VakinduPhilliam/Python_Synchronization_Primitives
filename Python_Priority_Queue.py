# Python Queue
# queue — A synchronized queue class.
# The queue module implements multi-producer, multi-consumer queues. It is especially useful in threaded programming when
# information must be exchanged safely between multiple threads.
# The Queue class in this module implements all the required locking semantics.
# class queue.PriorityQueue(maxsize=0) 
# Constructor for a priority queue. maxsize is an integer that sets the upperbound limit on the number of items that can be
# placed in the queue.
# Insertion will block once this size has been reached, until queue items are consumed.
# If maxsize is less than or equal to zero, the queue size is infinite.
# The lowest valued entries are retrieved first (the lowest valued entry is the one returned by sorted(list(entries))[0]).
# A typical pattern for entries is a tuple in the form: (priority_number, data).
# If the data elements are not comparable, the data can be wrapped in a class that ignores the data item and only compares the
# priority number:
 
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)

class PrioritizedItem:
    priority: int

    item: Any=field(compare=False)

