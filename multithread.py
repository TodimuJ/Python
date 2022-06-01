import time
import threading

def function_0():
    print("Thread 1: Is starting...")
    time.sleep(0.4)
    print("Thread 1: Is done!")


def function_1(arg=5):
    print("Thread 2: Is starting...")
    time.sleep(0.1)
    for num in range(arg):
        print(f"Thread 2: {num}")
        time.sleep(0.1)
    print("Thread 2: Is done!")


def function_2():
    print("Thread 3: Is starting...")
    while True:
        print("Thread 3: Daemon process running...")


