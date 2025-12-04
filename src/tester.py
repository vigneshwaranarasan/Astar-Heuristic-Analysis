import random
from graph import GridMap
from astar import astar_search
from heuristics import manhattan, euclidean

def generate_solvable_grid(width, height, obstacle_prob, min_cost, max_cost, seed):
    start = (0, 0)
    goal = (height - 1, width - 1)

    for attempt in range(30):
        grid = GridMap.random_grid(width, height, obstacle_prob, min_cost, max_cost, seed + attempt)
        grid.set_cost(start, min_cost)
        grid.set_cost(goal, min_cost)
        res = astar_search(grid, start, goal, manhattan)
        if res.found:
            return grid
    return grid

def run_experiments():
    random.seed(42)

    tests = [
        {"width": 20, "height": 20, "obstacle_prob": 0.20},
        {"width": 20, "height": 20, "obstacle_prob": 0.30},
        {"width": 25, "height": 25, "obstacle_prob": 0.25},
        {"width": 25, "height": 25, "obstacle_prob": 0.35},
        {"width": 30, "height": 30, "obstacle_prob": 0.20},
        {"width": 30, "height": 30, "obstacle_prob": 0.30},
        {"width": 35, "height": 35, "obstacle_prob": 0.25},
        {"width": 35, "height": 35, "obstacle_prob": 0.30},
        {"width": 40, "height": 40, "obstacle_prob": 0.22},
        {"width": 40, "height": 40, "obstacle_prob": 0.28},
    ]

    out = open("astar_raw_log.txt", "w")
    out.write("test_id,heuristic,found,path_length,total_cost,nodes_expanded,execution_time_ms,width,height,obstacle_prob\n")

    min_cost = 1.0
    max_cost = 5.0

    for i, cfg in enumerate(tests, 1):
        w, h, p = cfg["width"], cfg["height"], cfg["obstacle_prob"]

        grid = generate_solvable_grid(w, h, p, min_cost, max_cost, seed=1000+i)

        start = (0, 0)
        goal = (h-1, w-1)

        man = astar_search(grid, start, goal, manhattan)
        euc = astar_search(grid, start, goal, euclidean)

        out.write(f"{i},manhattan,{man.found},{len(man.path)},{man.total_cost},{man.nodes_expanded},{man.execution_time_ms},{w},{h},{p}\n")
        out.write(f"{i},euclidean,{euc.found},{len(euc.path)},{euc.total_cost},{euc.nodes_expanded},{euc.execution_time_ms},{w},{h},{p}\n")

    out.close()
    print("Log saved as astar_raw_log.txt")
