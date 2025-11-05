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

    # Sequential
    start_seq = time.time()
    seq_results = [worker_task(x) for x in tasks]
    end_seq = time.time()

    # Parallel
    start_par = time.time()
    with multiprocessing.Pool(processes=3) as pool:
        par_results = pool.map(worker_task, tasks)
    end_par = time.time()

    print("Input tasks:", tasks)
    print("Results:", par_results)
    print("Sequential execution time:", f"~{round(end_seq - start_seq, 1)} seconds")
    print("Total parallel execution time:", f"~{round(end_par - start_par, 1)} seconds")

