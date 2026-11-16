"""
Experiment 1: Breadth First Search (BFS) Algorithm
Scenario: A robot must find the shortest route to visit all rooms in a building level by level.
Expected Outcome: Explore nodes level-wise and find the shortest path in an unweighted graph.
"""

from collections import deque

def bfs_shortest_path(building_graph, start_room, target_room):
    visited = set([start_room])
    queue = deque([[start_room]])
    level_order = []

    while queue:
        path = queue.popleft()
        current_room = path[-1]
        if current_room not in level_order:
            level_order.append(current_room)

        if current_room == target_room:
            return path, level_order

        for neighbor in building_graph.get(current_room, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None, level_order

def bfs_all_rooms(building_graph, start_room):
    visited = set([start_room])
    queue = deque([(start_room, 0)])
    levels = {}

    while queue:
        room, level = queue.popleft()
        levels.setdefault(level, []).append(room)
        for neighbor in building_graph.get(room, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))
    return levels

if __name__ == "__main__":
    # Unweighted graph representing connected rooms in a building
    building = {
        "Entrance": ["Lobby", "Corridor_A"],
        "Lobby": ["Entrance", "Reception", "Server_Room"],
        "Corridor_A": ["Entrance", "Lab_1", "Lab_2"],
        "Reception": ["Lobby", "Conference_Hall"],
        "Server_Room": ["Lobby"],
        "Lab_1": ["Corridor_A", "Storage"],
        "Lab_2": ["Corridor_A"],
        "Conference_Hall": ["Reception"],
        "Storage": ["Lab_1"]
    }

    print("--- Level-by-Level Exploration from Entrance ---")
    levels = bfs_all_rooms(building, "Entrance")
    for lvl, rooms in levels.items():
        print(f"Level {lvl}: {rooms}")

    start, goal = "Entrance", "Storage"
    shortest_path, explored = bfs_shortest_path(building, start, goal)
    print(f"\nShortest Route from '{start}' to '{goal}': {' -> '.join(shortest_path)}")
