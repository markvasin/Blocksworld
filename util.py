import heapq
from collections import deque


class Queue:

    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


class PriorityQueue:

    def __init__(self):
        self.queue = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.queue, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.queue)
        return item

    def is_empty(self):
        return len(self.queue) == 0
