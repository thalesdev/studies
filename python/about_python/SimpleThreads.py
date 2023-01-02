import _thread as thread
import time

# Travando treads

def th1():

    def count(threadId, count):
        for i in range(count):
            time.sleep(1)
            mutex.acquire() # Boquea o uso das variaveis usadas nas linhas a baixo
            print("[{0:^5}] => {1:^5}".format(threadId, i))
            mutex.release() # Libera o uso


    mutex = thread.allocate_lock()
    for i in range(5):
        thread.start_new_thread(count, (i, 5))

    time.sleep(6)
    print("Exit from main thread...")



##################### de um maneira melhor
def th2():
    stdout_lock = thread.allocate_lock()
    threads_alive = [True for _ in range(5)]
    def counter(threadId, times):
        for i in range(times):
            stdout_lock.acquire() # toma o controle das variaveis a baixo
            print("[{0:^5}] => {1:^5}".format(threadId, i))
            stdout_lock.release() # libera o controle das variaveis abaixo
        threads_alive[threadId] = False
    for i in range(5):
        thread.start_new_thread(counter, (i,100))
    while True in threads_alive: pass
    print("Programa terminou com sucesso")




th2()