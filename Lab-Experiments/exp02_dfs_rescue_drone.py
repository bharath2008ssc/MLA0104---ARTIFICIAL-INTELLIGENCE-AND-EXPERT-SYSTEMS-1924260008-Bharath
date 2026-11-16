"""
Experiment 2: Depth First Search (DFS) Algorithm
Scenario: A rescue drone explores a cave by moving as deep as possible before backtracking.
Expected Outcome: Traverse nodes using depth-first exploration.
"""

def dfs_explore_cave(cave_map, current_chamber, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    visited.add(current_chamber)
    traversal_order.append(current_chamber)

    for next_chamber in cave_map.get(current_chamber, []):
        if next_chamber not in visited:
            dfs_explore_cave(cave_map, next_chamber, visited, traversal_order)

    return traversal_order

def dfs_find_survivor(cave_map, start, target, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == target:
        return path

    for neighbor in cave_map.get(start, []):
        if neighbor not in visited:
            result = dfs_find_survivor(cave_map, neighbor, target, path, visited)
            if result:
                return result
    return None

if __name__ == "__main__":
    cave = {
        "Cave_Mouth": ["Tunnel_North", "Tunnel_East"],
        "Tunnel_North": ["Crystal_Cavern", "Underground_River"],
        "Crystal_Cavern": ["Deep_Abyss"],
        "Deep_Abyss": [],
        "Underground_River": ["Hidden_Chamber"],
        "Hidden_Chamber": [],
        "Tunnel_East": ["Bat_Roost", "Collapsed_Shaft"],
        "Bat_Roost": [],
        "Collapsed_Shaft": []
    }

    order = dfs_explore_cave(cave, "Cave_Mouth")
    print("Rescue Drone Depth-First Exploration Order:")
    print(" -> ".join(order))

    survivor_location = "Hidden_Chamber"
    rescue_path = dfs_find_survivor(cave, "Cave_Mouth", survivor_location)
    print(f"\nPath found to survivor at '{survivor_location}': {' -> '.join(rescue_path)}")
