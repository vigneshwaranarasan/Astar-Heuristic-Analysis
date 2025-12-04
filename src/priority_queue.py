from typing import Tuple, List
import heapq

Coord = Tuple[int, int]

class PriorityQueue:
    """Min-priority queue using heapq."""

    def __init__(self) -> None:
        self._heap: List[Tuple[float, int, Coord]] = []
        self._counter = 0  # to break ties

    def push(self, priority: float, item: Coord) -> None:
        self._counter += 1
        heapq.heappush(self._heap, (priority, self._counter, item))

    def pop(self) -> Coord:
        priority, _, item = heapq.heappop(self._heap)
        return item

    def empty(self) -> bool:
        return not self._heap
