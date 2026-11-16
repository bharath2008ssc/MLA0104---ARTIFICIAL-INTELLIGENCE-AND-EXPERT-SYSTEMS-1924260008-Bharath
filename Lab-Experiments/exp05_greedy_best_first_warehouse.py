"""
Experiment 5: Greedy Best First Search Algorithm
Scenario: A warehouse robot chooses the nearest storage rack at every step to minimize travel time.
Expected Outcome: Solve pathfinding using greedy heuristics.
"""

import heapq

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def greedy_warehouse_path(grid, start, target_rack):
    rows, cols = len(grid), len(grid[0])
    open_set = [(manhattan_distance(start, target_rack), start, [start])]
    visited = set()

    while open_set:
        _, current, path = heapq.heappop(open_set)

        if current == target_rack:
            return path

        if current in visited:
            continue
        visited.add(current)

        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                if (nr, nc) not in visited:
                    h = manhattan_distance((nr, nc), target_rack)
                    heapq.heappush(open_set, (h, (nr, nc), path + [(nr, nc)]))

    return None

if __name__ == "__main__":
    # 0 = Open Aisle, 1 = Occupied Storage Rack Obstacle
    warehouse_floor = [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    robot_start = (0, 0)
    target_rack = (4, 4)

    path = greedy_warehouse_path(warehouse_floor, robot_start, target_rack)
    print(f"Warehouse Robot Greedy Path from {robot_start} to {target_rack}:")
    print(path)
