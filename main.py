# Assignment: Simulating a Distributed Task Execution System
# Name: 24915 JDT Dilshan / 24452 WPDSM Weerasinghe

import multiprocessing
import time
import networkx as nx
import matplotlib.pyplot as plt

def worker_task(x):
    time.sleep(0.5)
    return x * x

if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6]

    start_time = time.time()
    results = [worker_task(x) for x in tasks]
    end_time = time.time()

    print("Input tasks:", tasks)
    print("Sequential results:", results)
    print("Sequential execution time:", round(end_time - start_time, 2), "seconds")
