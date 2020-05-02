import heapq
import random


class Stack:
    pass


class Node:
    next = None
    pass


if __name__ == "__main__":
    # stack = Stack()
    # stack.push(4)
    # assert 4 == stack.pop()
    h = []
    for i in range(1, 100):
        heapq.heappush(h, random.randrange(1, 100))
    print(h)
    print(heapq.heappop(h))
