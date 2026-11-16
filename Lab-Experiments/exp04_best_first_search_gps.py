"""
Experiment 4: Best First Search Algorithm
Scenario: A GPS navigation system selects the next city based on the estimated distance to the destination.
Expected Outcome: Find a path using heuristic evaluation.
"""

import heapq

def best_first_search(city_graph, heuristics, start_city, goal_city):
    # Priority queue ordered solely by heuristic h(n)
    open_list = [(heuristics[start_city], start_city, [start_city])]
    visited = set()

    while open_list:
        h_val, current, path = heapq.heappop(open_list)

        if current == goal_city:
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor in city_graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristics[neighbor], neighbor, path + [neighbor]))

    return None

if __name__ == "__main__":
    road_map = {
        "City_A": ["City_B", "City_C"],
        "City_B": ["City_A", "City_D", "City_E"],
        "City_C": ["City_A", "City_F"],
        "City_D": ["City_B", "City_G"],
        "City_E": ["City_B", "City_G"],
        "City_F": ["City_C", "City_G"],
        "City_G": []
    }

    # Straight-line estimated distance (heuristic) to City_G
    estimated_distance_to_goal = {
        "City_A": 40,
        "City_B": 32,
        "City_C": 25,
        "City_D": 18,
        "City_E": 12,
        "City_F": 15,
        "City_G": 0
    }

    route = best_first_search(road_map, estimated_distance_to_goal, "City_A", "City_G")
    print("GPS Navigation Path (Best-First Search):", " -> ".join(route))
