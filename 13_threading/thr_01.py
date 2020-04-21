import threading
import datetime
from time import sleep

class myThread (threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"Starting {self.name}")
        print_date(thread_name=self.name)
        print(f"Finishing {self.name}")

def print_date(thread_name):
    today = datetime.date.today()
    # if thread_name == "Thread 1":
    #     sleep(2)
    print(f'{thread_name}: {today}')

# Создание новых потоков
thread1 = myThread(name="Thread 1")
thread2 = myThread(name="Thread 2")

# Запуск новых потоков
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Threads are dead")
