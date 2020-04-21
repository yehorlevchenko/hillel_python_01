from multiprocessing import Process, Lock
from random import randint
from os import getpid
from time import sleep

# define a example function
def work(i, lock):
    lock.acquire()
    sleep(randint(0,2))
    print(f"Firing {getpid()}, which is a process #{i}")
    lock.release()

lock = Lock()

# Setup a list of processes
processes = list()
for p in range(10):
    process = Process(target=work, args=(p, lock))
    processes.append(process)

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()
