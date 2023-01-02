import threading
import time
import os
import random

def father(pipeIn, id, mutex, read_bytes=32):
        while True:
            data = os.read(pipeIn, read_bytes)
            with mutex:
                print("Father {0:^10} received {1} as {2}".format(id, data, time.time()))


def son(pipeOut, max_counter=5):
        counter = 0
        while True:
            time.sleep(0.01 * random.random())
            msg = "Spam {}".format(counter).encode()
            os.write(pipeOut, msg)
            counter = (counter+1) % max_counter

def anounsPipes():
    """
        Pipe anonimo otimo pra intercomunicação entre threads do mesmo processo...
        Com subprocess da pra dibrar isso porem o processo tem que ser chamado pelo main process... 
        but da pra criar usando o Win32Pipe um pipe nomeado porem da trabalho....
    """
    mutex = threading.Lock()
    num_fathers = 2
    pipeIn, pipeOut = os.pipe()
    fathers = []

    threading.Thread(target=son, args=(pipeOut,)).start()

    for i in range(num_fathers):
        fat = threading.Thread(target=father, args=(pipeIn, i, mutex))
        fat.start()
        fathers.append(fat)




