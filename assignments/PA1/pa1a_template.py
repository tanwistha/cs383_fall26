"""
PA1a - Environment Check + Stack & Queue Basics
CS 383 - Algorithm Analysis and Design 
"""

import sys

YOUR_NAME_HERE = "YOUR_NAME_HERE"  # <-- replace with your name


def environment_check():
    """
    PART 0 — Environment Check

    Do not change this function. Just make sure it runs without errors
    when you execute this file directly (see the bottom of this file).
    """
    version = sys.version_info
    print(f"Hello, {YOUR_NAME_HERE}! You are running Python {version.major}.{version.minor}.")


class Stack:
    """
    PART 1 — Stack (LIFO: Last-In-First-Out)

    Backed by a Python list. Do not use collections.deque or any other
    built-in stack/queue type — the point is to see how push/pop map
    onto a plain list.
    """

    def __init__(self):
        self._items = []

    def push(self, item):
        """Add item to the top of the stack."""
        # TODO
        raise NotImplementedError

    def pop(self):
        """Remove and return the item at the top. Raise IndexError if empty."""
        # TODO
        raise NotImplementedError

    def peek(self):
        """Return (without removing) the item at the top. Raise IndexError if empty."""
        # TODO
        raise NotImplementedError

    def is_empty(self):
        """Return True if the stack has no items."""
        # TODO
        raise NotImplementedError

    def size(self):
        """Return the number of items in the stack."""
        # TODO
        raise NotImplementedError


class Queue:
    """
    PART 2 — Queue (FIFO: First-In-First-Out)

    Backed by a Python list.
    """

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Add item to the back of the queue."""
        # TODO
        raise NotImplementedError

    def dequeue(self):
        """Remove and return the item at the front. Raise IndexError if empty."""
        # TODO
        raise NotImplementedError

    def peek(self):
        """Return (without removing) the item at the front. Raise IndexError if empty."""
        # TODO
        raise NotImplementedError

    def is_empty(self):
        """Return True if the queue has no items."""
        # TODO
        raise NotImplementedError

    def size(self):
        """Return the number of items in the queue."""
        # TODO
        raise NotImplementedError


# =====================================================================
# PART 3 — Written answer (required)
# =====================================================================
# Q: In your own words, what's the difference between a stack and a
#    queue? Give one real-world example of each (not from lecture).
#
# A: <YOUR ANSWER HERE — 2 to 3 sentences>
# =====================================================================


if __name__ == "__main__":
    environment_check()

    # Quick manual sanity checks — feel free to add more while debugging.
    s = Stack()
    s.push(1)
    s.push(2)
    print("Stack size:", s.size())   # expect 2
    print("Stack pop:", s.pop())     # expect 2

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("Queue size:", q.size())   # expect 2
    print("Queue dequeue:", q.dequeue())  # expect 1
