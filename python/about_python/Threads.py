# Threading de vdd
from datetime import datetime
from threading import Thread, Lock
from tqdm import tqdm

"""
class MyThread(Thread):
    def __init__(self, threadId, times, mutex):
        super(MyThread, self).__init__()
        self.threadId = threadId
        self.times = times
        self.mutex = mutex
        self.alive = False

    def run(self):
        self.alive = True
        for i in range(self.times):
            with self.mutex:
                print("[{0:^3}] => {1:^3}".format(self.threadId, i))
        self.alive = False


num_threads = 10
stdoutmutex = Lock()
threads = []
times = 100

for i in range(num_threads):
    thread = MyThread(i, times, stdoutmutex)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print("Exit from main thread.")
"""


def ex(nums, num_threads):
    """
        O arquivo txt possui multiplas linhas contendo números
        Escreva um objeto thread que consiga acessar uma linha
        especifíca do arquivo e le-lo até certo ponto de forma
        a obter a soma dos números contidos dentro do arquivo.
    """

    batch_size = (len(nums)//num_threads)
    threads = []
    counter_mutex = Lock()
    results = []
    for i in range(num_threads):
        batch = nums[i*batch_size:((i+1)*batch_size)]
        thread = SumThread(i, batch, counter_mutex, results)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


class SumThread(Thread):
    def __init__(self, threadId, nums, mutex, result):
        super(SumThread, self).__init__()
        self.threadId = threadId
        self.nums = nums
        self.mutex = mutex
        self.result = result

    def run(self):
        res = sum(map(lambda e: int(e), self.nums))
        with self.mutex:
            self.result.append(res)


with open("num.txt") as pointer:
    data = pointer.readlines()
    values = []
    times = 5
    for time in range(times):
        init = datetime.now()
        ex(data, 10)
        end = datetime.now()
        values.append((end-init).microseconds)
    mean = sum(values)/len(values) * 1e-6
    print("O processamento teve media de {0:.2}s".format(mean))