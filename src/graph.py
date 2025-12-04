from typing import Tuple, List, Optional
import random

Coord = Tuple[int, int]

class GridMap:
    """
    Weighted 2D grid graph.
    - cost <= 0 => obstacle
    - cost > 0  => traversable
    """

    def __init__(self, width: int, height: int, default_cost: float = 1.0):
        self.width = width
        self.height = height
        self._cells = [
            [default_cost for _ in range(width)] for _ in range(height)
        ]

    def in_bounds(self, coord: Coord) -> bool:
        r, c = coord
        return 0 <= r < self.height and 0 <= c < self.width

    def is_blocked(self, coord: Coord) -> bool:
        r, c = coord
        return self._cells[r][c] <= 0

    def cost(self, coord: Coord) -> float:
        r, c = coord
        return self._cells[r][c]

    def set_cost(self, coord: Coord, value: float):
        r, c = coord
        self._cells[r][c] = value

    def neighbors(self, coord: Coord) -> List[Coord]:
        r, c = coord
        candidates = [
            (r-1, c), (r+1, c),
            (r, c-1), (r, c+1)
        ]
        result = []
        for nr, nc in candidates:
            if self.in_bounds((nr, nc)) and not self.is_blocked((nr, nc)):
                result.append((nr, nc))
        return result

    @staticmethod
    def random_grid(width, height, obstacle_prob, min_cost, max_cost, seed=None):
        if seed is not None:
            random.seed(seed)

        grid = GridMap(width, height)
        for r in range(height):
            for c in range(width):
                if random.random() < obstacle_prob:
                    grid.set_cost((r, c), 0.0)
                else:
                    grid.set_cost((r, c), random.uniform(min_cost, max_cost))
        return grid
