# *=> imports
import search
import time
from plot import *
from collections import namedtuple

# *=> constants

SHOW_TERMINAL=True
SHOW_PLOT=True

TEST_REPEAT=100

algorithm = namedtuple("Algorithm", "name func")

algorithms = [
    algorithm("DEPTH", search.depth_first_graph_search),
    algorithm("BREADTH",         search.breadth_first_graph_search),
    algorithm("BRANCH & BOUND",  search.branch_and_bound_graph_search),
    algorithm("HEURISTIC",       search.heuristic_graph_search)
]

PROBLEMS=[
    ["A","B"],
    ["O","E"],
    ["G","Z"],
    ["N","D"],
    ["M","F"]
]

# variables
times = [0 for _ in algorithms]



# *=> functions

def test_search(func, title):
    if SHOW_TERMINAL: print(f"\n\t# {title}")
    tmp=time.perf_counter_ns()
    
    for i in range(1, TEST_REPEAT): func(False)
        
    node=func(SHOW_TERMINAL)
    
    tmp= (time.perf_counter_ns()-tmp)*0.001/TEST_REPEAT

    if SHOW_TERMINAL: print("\n\tTiempo de ejecución: ", tmp , "µs")
    if SHOW_TERMINAL: print("\tCoste total:",node.path_cost, "-", node.path())

    return tmp

def test_problem(problem, title):
    if SHOW_TERMINAL: print(f"# {title} =================================================================")
    for i in range(0, len(algorithms)):
        times[i]+= test_search(lambda show: algorithms[i].func(problem, show), algorithms[i].name)
    if SHOW_TERMINAL: print()


# *=> run

if SHOW_TERMINAL: print()

for elm in PROBLEMS:
    test_problem(search.GPSProblem(elm[0], elm[1], search.romania), f"{elm[0]}-{elm[1]}")

for idx in range(0, len(times)): times[idx]/=len(times)

if SHOW_PLOT: plot([i for i in range(len(algorithms))],times, [elm.name for elm in algorithms], "Tiempo de ejecucion (µs)")