"""
Experiment 3: Uniform Cost Search (UCS) Algorithm
Scenario: A logistics company wants to deliver goods with the minimum transportation cost.
Expected Outcome: Find the least-cost path between source and destination.
"""

import heapq

def uniform_cost_search(network, source, destination):
    # Priority queue stores (cumulative_cost, current_city, path_taken)
    priority_queue = [(0, source, [source])]
    visited_costs = {}

    while priority_queue:
        cost, current_city, path = heapq.heappop(priority_queue)

        if current_city == destination:
            return cost, path

        if current_city in visited_costs and visited_costs[current_city] <= cost:
            continue

        visited_costs[current_city] = cost

        for neighbor, transport_cost in network.get(current_city, []):
            new_cost = cost + transport_cost
            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))

    return float("inf"), []

if __name__ == "__main__":
    logistics_network = {
        "Warehouse_Chennai": [("Hub_Vellore", 140), ("Hub_Pondicherry", 150)],
        "Hub_Vellore": [("Hub_Krishnagiri", 120), ("Hub_Salem", 210)],
        "Hub_Pondicherry": [("Hub_Trichy", 200)],
        "Hub_Krishnagiri": [("Destination_Bangalore", 90)],
        "Hub_Salem": [("Destination_Bangalore", 200), ("Hub_Trichy", 140)],
        "Hub_Trichy": [("Destination_Bangalore", 340)],
        "Destination_Bangalore": []
    }

    src, dst = "Warehouse_Chennai", "Destination_Bangalore"
    min_cost, optimal_route = uniform_cost_search(logistics_network, src, dst)
    print(f"Optimal Logistics Route from {src} to {dst}:")
    print("Route:", " -> ".join(optimal_route))
    print(f"Minimum Transportation Cost: ${min_cost}")
