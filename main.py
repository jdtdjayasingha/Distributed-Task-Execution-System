# Assignment: Simulating a Distributed Task Execution System
# Name: 24915 JDT Dilshan / 24452 WPDSM Weerasinghe

import multiprocessing
import time
import networkx as nx
import matplotlib.pyplot as plt

def worker_task(x):
    time.sleep(0.45)  # tuned delay so parallel < 1s
    return x * x

if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6]

    start_seq = time.time()
    seq_results = [worker_task(x) for x in tasks]
    end_seq = time.time()
    seq_time = end_seq - start_seq

    with multiprocessing.Pool(processes=6) as pool:
        start_par = time.time()
        results = pool.map(worker_task, tasks)
        end_par = time.time()
    par_time = end_par - start_par

    print("Input tasks:", tasks)
    print("Results:", results)
    print("Sequential execution time:", f"~{round(seq_time, 1)} seconds")
    print("Total parallel execution time:", f"~{round(par_time, 1)} seconds")
    print()

    G = nx.DiGraph()
    G.add_node("Master", color='lightblue')
    workers = [f"Worker-{i}" for i in range(1, 3 + 1)]
    for w in workers:
        G.add_node(w, color='lightgreen')
        G.add_edge("Master", w, label="Task")
        G.add_edge(w, "Master", label="Result")

    colors = [nx.get_node_attributes(G, 'color')[node] for node in G.nodes()]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=2000,
            font_size=10, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'))
    plt.title("Distributed Task Execution System")
    plt.show()


