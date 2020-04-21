from multiprocessing import Process, Pipe
from random import randint
from os import getpid
from time import sleep

# define a example function
def work(child_conn, parent_conn):
    while True:
        sleep(randint(0,2))
        print(f"{getpid()} wakes up")
        process_1.child_conn.send(f"Hello from {getpid()}")
        print(f"{getpid()} receiving: {process_1.parent_conn.recv()}")
        print(f"{getpid()} sleeps")

# Setup a list of processes
parent_conn_1, child_conn_1 = Pipe()
parent_conn_2, child_conn_2 = Pipe()

process_1 = Process(target=work, args=(child_conn_1, parent_conn_2)).start()
process_2 = Process(target=work, args=(child_conn_2, parent_conn_1)).start()
