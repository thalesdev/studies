import time
from threading import Lock, Thread
from queue import Queue, Empty as QueueEmpty


class Producer(Thread):
    def __init__(self, producer_id, queue, num_mesages):
        super(Producer, self).__init__()
        self.num_mesages = num_mesages
        self.producer_id = producer_id
        self.queue = queue

    def run(self):
        for i in range(self.num_mesages):
            self.queue.put(
                "[Producer id={0:^4}, cont={1:^4}]".format(self.producer_id, i))


class Customer(Thread):
    def __init__(self, id, queue, mutex):
        super(Customer, self).__init__()
        self.id = id
        self.mutex = mutex
        self.queue = queue

    def run(self):
        while True:
            try:
                data = self.queue.get(block=False)
            except QueueEmpty as qd:
                pass
            else:
                with self.mutex:
                    print("Customer {0:^4} received => {1}".format(
                        self.id, data))


num_producers = 2
num_customers = 5
num_msg_producers = 5
queue = Queue()
mutex = Lock()

for i in range(num_customers):
    custo = Customer(i, queue, mutex)
    custo.daemon = True # Quando a thread principal ele mata essa thread mesmo que ela nao tenha terminado
    custo.start()

wait = []

for i in range(num_producers):
    prod = Producer(i, queue, num_msg_producers)
    prod.start()
    wait.append(prod)


for thread in wait: thread.join() # espera as threads acabarem
with mutex:
    print("O programa acabou mermao")