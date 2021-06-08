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






if __name__ == "__main__":
    t = time.time()
    orders = ['pizza','samosa','pasta','biryani','burger']

    T1 = threading.Thread(target=Place_order, args=(orders,))
    T2 = threading.Thread(target=Serve_order)



    T1.start()

    T2.start()

    T1.join()
    T2.join()

    print("done in : ", time.time() - t)
    print("Hah... I am done with all my work now!")


