import os
import time, datetime
import multiprocessing as mp
from multiprocessing import Process, Lock, Pipe, JoinableQueue, Queue, Event, Pool


def who_i_am(label, lock):

    for _ in range(50):
        time.sleep(0.5)
        with lock:
            print("{0}: name:{1}, pid:{2}".format(
                label, __name__, os.getpid()))


def comunicate(pipe):
    pipe.send(dict(name="Batman", age=32))
    response = pipe.recv()
    print('comunicate received {}'.format(response))


def sender(pipe):
    pipe.send(['spam'] + ['42', 'eggs'])
    pipe.close()


def teste():
    """ Multiprocessing basico no windows cria novos interpretadores e no unix usa o fork"""
    lock = Lock()
    process = []
    for _ in range(10):
        P = Process(target=who_i_am, args=("sla {}".format(_), lock))
        P.start()
        process.append(P)
    for p in process:
        p.join()


def teste2():
    """ Comunicacao via Pipes """
    _output, _input = Pipe()
    Process(target=sender, args=(_input,)).start()
    print("Sender Output received : {}".format(_output.recv()))
    _output.close()

    _output, _input = Pipe()
    pro = Process(target=comunicate, args=(_input,))
    pro.start()
    print("Comunicate output received :{}".format(_output.recv()))
    _output.send({x * 2 for x in "spam"})
    pro.join()

#### Queues #####


class Customer(Process):

    def __init__(self, tasks, results):
        super(Customer, self).__init__()
        self.tasks = tasks
        self.results = results

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.tasks.get()
            if next_task is None:
                print("{} exiting...".format(proc_name))
                self.tasks.task_done()
                break
            print("{}:{}".format(proc_name, next_task))
            response = next_task()
            self.tasks.task_done()
            self.results.put(response)
        return


class Task(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        time.sleep(0.1)
        return "{0:^3} * {1:^3} = {2:^4}".format(self.a, self.b, self.a * self.b)

    def __str__(self):
        return "{0:^3} * {1:^3}".format(self.a, self.b)


def teste3():
    """ Comunicacao via quees """
    tasks = JoinableQueue()
    results = Queue()
    num_customers = mp.cpu_count() * 2
    num_tasks = 10
    customers = [
        Customer(tasks, results) for _ in range(num_customers)
    ]
    for c in customers:
        c.start()
    for i in range(num_tasks):
        tasks.put(Task(i, i))
    for i in range(num_customers):
        tasks.put(None)

    tasks.join()
    print("")
    while num_tasks:
        response = results.get()
        print("Result : {0}".format(response))
        num_tasks -= 1


def wait_for_event(e):
    """ Espera o evento  antes de processeguir """
    print("wait_for_event: started")
    e.wait()
    print("wait_for_event: e.is_set() -> {}".format(e.is_set()))


def wait_for_timeout_event(e, t):
    """ Espera t segundos e depois timeout """
    print("wait_for_timeout_event: started")
    e.wait(t)
    print("wait_for_timeout_event: e.is_set() -> {}".format(e.is_set()))


def teste4():
    """ Comunicacao via events representa dois estados unset e set """
    e = Event()
    w1 = Process(name='bloco-1', target=wait_for_event, args=(e,))
    w1.start()

    w2 = Process(name="bloco-2", target=wait_for_timeout_event, args=(e, 2))
    w2.start()

    print("Main thread waits from Event.set...")
    time.sleep(3)
    e.set()
    print("Main thread is ready..")


def init():
    print(
        "Starting {}".format(mp.current_process().name))


def x2(x): return x*2


def teste5():
    """Utilizando pools  eles distribuem os processos pelos recursos disponiveis no computador"""
    num_pools = mp.cpu_count() * 2
    start = datetime.datetime.now()
    inputs = range(1000000000)
    print("Inputs : {}...".format(inputs))
    print("built-in outputs : 2*{0}...".format(inputs))
    pool = Pool()
    pool_outputs = pool.map_async(x2, inputs)
    pool.terminate()

    with pool:
        end = datetime.datetime.now()
        print("execution time from pool: {}".format(  (end-start).microseconds  * 1e-6  ))
        



if __name__ == "__main__":
    # lock = Lock()
    # who_i_am("Startando os processos bro...", lock)
    # P = Process(target=who_i_am, args=("Son created sucessfull.", lock))
    # P.start()
    # P.join()
    # mp(lock, who_i_am)
    teste5()
