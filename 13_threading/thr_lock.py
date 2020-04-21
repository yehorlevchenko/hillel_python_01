import threading
import datetime
from time import sleep


class myThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print (f"Starting {self.name}")
        threadLock.acquire(blocking=False, timeout=-1)
        print_date(self.name)
        if threadLock.locked():
            threadLock.release()
        print (f"Finishing {self.name}")

def print_date(thread_name):
    today = datetime.date.today()
    if thread_name == "Thread 1":
        sleep(2)
    print(f"{thread_name}: {today}")

threadLock = threading.Lock()
threads = []

thread1 = myThread("Thread 1")
thread2 = myThread("Thread 2")

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print("Threads are dead")
