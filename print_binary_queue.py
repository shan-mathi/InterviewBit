from collections import deque
import time
import threading

class Queue():
    def __init__(self):
        self.Q = deque()
    def dequeue(self):
        return self.Q.pop()
    def enqueue(self,val):
        self.Q.appendleft(val)
    def size(self):
        return len(self.Q)
    def peek(self):
        return self.Q[-1]
    def is_empty(self):
        return len(self.Q)==0

Q = Queue()
def Place_order(order):
    for order in orders:
        print("Placing order for:",order)

        Q.enqueue(order)
        time.sleep(0.5)

def Serve_order():
    time.sleep(1)
    while not Q.is_empty():
        order = Q.dequeue()
        print("Now serving ",order)
        time.sleep(1)





def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.peek()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


if __name__ == '__main__':
    produce_binary_numbers(20)

