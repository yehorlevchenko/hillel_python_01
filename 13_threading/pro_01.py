import multiprocessing as mp
import random
from os import getpid

# output queue
output = mp.Queue()

# define a example function
def work(count, output):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    data = list()
    for i in range(count):
        data.append(i)
    data.append(f'Author: {getpid()}')
    output.put(data)

# Setup a list of processes
processes = list()
for p in range(4):
    process = mp.Process(target=work, args=(3, output))
    processes.append(process)

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
results = [output.get() for p in processes]

print(results)
