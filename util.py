from collections import deque


class Queue:
    """FIFO queue"""

    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0


class Stack:
    """LIFO stack"""

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
