"""
Experiment 6: A* Search Algorithm
Scenario: A delivery robot must reach its destination using both actual travel cost and estimated remaining distance.
Expected Outcome: Obtain the optimal path using heuristic and path cost.
"""

import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority queue holds (f_cost = g_cost + h_cost, g_cost, current_node, path)
    open_list = [(heuristics[start], 0, start, [start])]
    g_scores = {start: 0}

    while open_list:
        f_cost, g_cost, current, path = heapq.heappop(open_list)

        if current == goal:
            return g_cost, path

        for neighbor, step_cost in graph.get(current, []):
            tentative_g = g_cost + step_cost
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristics[neighbor]
                heapq.heappush(open_list, (f_score, tentative_g, neighbor, path + [neighbor]))

    return float("inf"), []

if __name__ == "__main__":
    campus_graph = {
        "Docking_Station": [("Main_Hall", 4), ("Courtyard", 2)],
        "Main_Hall": [("Docking_Station", 4), ("Office_Wing", 5), ("Cafeteria", 10)],
        "Courtyard": [("Docking_Station", 2), ("Garden_Path", 3)],
        "Garden_Path": [("Courtyard", 3), ("Office_Wing", 2)],
        "Office_Wing": [("Main_Hall", 5), ("Garden_Path", 2), ("Executive_Suite", 4)],
        "Cafeteria": [("Main_Hall", 10), ("Executive_Suite", 1)],
        "Executive_Suite": []
    }

    heuristic_to_suite = {
        "Docking_Station": 10,
        "Main_Hall": 8,
        "Courtyard": 8,
        "Garden_Path": 5,
        "Office_Wing": 3,
        "Cafeteria": 1,
        "Executive_Suite": 0
    }

    total_cost, optimal_path = a_star_search(campus_graph, heuristic_to_suite, "Docking_Station", "Executive_Suite")
    print("A* Optimal Delivery Route:", " -> ".join(optimal_path))
    print(f"Total Optimal Travel Cost: {total_cost} units")
