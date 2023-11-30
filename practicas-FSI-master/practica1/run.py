# *=> imports
import search
import time
from plot import *

# *=> constants

SHOW_TERMINAL=True
SHOW_PLOT=True

TEST_REPEAT=100

PROBLEMS=[
    ["A","B"],
    ["O","E"],
    ["G","Z"],
    ["N","D"],
    ["M","F"]
]
ALGORITHMS=[
    "DEPTH",
    "BREADTH",
    "BRANCH & BOUND",
    "HEURISTIC"
]
ALGORITHMS_FUNC=[
    search.depth_first_graph_search,
    search.breadth_first_graph_search,
    search.branch_and_bound_graph_search,
    search.heuristic_graph_search
]

# variables
times = [0 for i in ALGORITHMS]


# *=> functions

def test_search(func, title):
    if SHOW_TERMINAL: print(f"\n\t# {title}")
    tmp=time.perf_counter_ns()
    
    for i in range(1, TEST_REPEAT): func(False)
        
    node=func(SHOW_TERMINAL)
    
    tmp= (time.perf_counter_ns()-tmp)*0.001/TEST_REPEAT

    if SHOW_TERMINAL: print("\tTiempo de ejecución: ", tmp , "µs")
    if SHOW_TERMINAL: print("\tCoste total:",node.path_cost, "-", node.path())

    return tmp

def test_problem(problem, title):
    if SHOW_TERMINAL: print(f"# {title} =================================================================")
    for i in range(0, len(ALGORITHMS)):
        times[i]+= test_search(lambda show: ALGORITHMS_FUNC[i](problem, show), ALGORITHMS[i])
    if SHOW_TERMINAL: print()


# *=> run

if SHOW_TERMINAL: print()

for elm in PROBLEMS:
    title=f"{elm[0]}-{elm[1]}"
    test_problem(search.GPSProblem(elm[0], elm[1], search.romania), title)

for idx in range(0, len(times)): times[idx]/=len(times)

if SHOW_PLOT: plot([i for i in ALGORITHMS],times, ALGORITHMS, "Tiempo de ejecucion (µs)")