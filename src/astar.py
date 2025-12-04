from dataclasses import dataclass
from typing import Dict, List, Tuple, Callable
import math
import time

from priority_queue import PriorityQueue
from graph import GridMap

Coord = Tuple[int, int]
HeuristicFn = Callable[[Coord, Coord], float]

@dataclass
class AStarResult:
    found: bool
    path: List[Coord]
    total_cost: float
    nodes_expanded: int
    execution_time_ms: float

def reconstruct_path(came_from, start, goal):
    if goal not in came_from and goal != start:
        return []
    path = [goal]
    curr = goal
    while curr != start:
        curr = came_from[curr]
        path.append(curr)
    return list(reversed(path))

def astar_search(grid: GridMap, start: Coord, goal: Coord, heuristic: HeuristicFn) -> AStarResult:
    t0 = time.perf_counter()

    if grid.is_blocked(start) or grid.is_blocked(goal):
        return AStarResult(False, [], math.inf, 0, 0)

    open_set = PriorityQueue()
    open_set.push(0, start)

    came_from = {}
    g_cost = {start: 0.0}
    nodes_expanded = 0

    while not open_set.empty():
        current = open_set.pop()
        nodes_expanded += 1

        if current == goal:
            path = reconstruct_path(came_from, start, goal)
            t1 = time.perf_counter()
            return AStarResult(True, path, g_cost[goal], nodes_expanded, (t1 - t0)*1000)

        for neighbor in grid.neighbors(current):
            new_cost = g_cost[current] + grid.cost(neighbor)

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                came_from[neighbor] = current
                priority = new_cost + heuristic(neighbor, goal)
                open_set.push(priority, neighbor)

    t1 = time.perf_counter()
    return AStarResult(False, [], math.inf, nodes_expanded, (t1 - t0)*1000)
