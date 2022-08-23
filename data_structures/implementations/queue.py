# a queue is a FIFO data structure (first in first out)
# it allows for loosely coupled architecture, which is good for producer/consumer problems
from collections import deque
class Queue:
    # initializes the queue as a dequeue
    def __init__(self):
        self.buffer = deque()

    # adds a value to the queue at position 0
    def enqueue(self, value):
        self.buffer.appendleft(value)

    #returns the first item added to the queue
    def dequeue(self):
        return self.buffer.pop()

    # returns true if the queue is empty
    def is_empty(self):
        return len(self.buffer) == 0

    # returns the size of the queue
    def size(self):
        return len(self.buffer)

# EXAMPLE
price_queue = Queue()

price_queue.enqueue({
    'company': 'AAPL',
    'timestamp': '08/16/2022 8:50 AM',
    'price': '175'
    }, {'company': 'MSFT'})

print(price_queue.dequeue()) # prints out the above info for AAPL stock when executed

# Exercise 1. Design a food ordering system that runs on two threads



