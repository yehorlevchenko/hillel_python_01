from multiprocessing import Process, Pipe
from time import sleep
from os import getpid

def ponger(receiver, sender, response):
    while True:
        # receive a message
        # print it as f"Process{getpid()} got message: {msg}"
        # sleep before responding
        # send response message back

if __name__ == "__main__":
    # create 2 pipes
    # create 2 processes that will use ponger, give them different sides of pipes
    # they also need a specific message (either ping or pong)
    # start both processes
    # initiate ping-pong by sending first message to one of the pipes
