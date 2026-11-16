"""
Experiment 25: Best First Search (Prolog-style Logic Engine in Python)
Scenario: A search application written in Prolog locates the best route using heuristic information.
Expected Outcome: Perform heuristic search using Prolog-style declarative facts and rules.
"""

# Declarative Prolog-style Knowledge Base: edge(From, To, Cost) and h(Node, Heuristic)
EDGES = [
    ("home", "station", 2),
    ("home", "park", 4),
    ("station", "library", 5),
    ("park", "library", 2),
    ("library", "university", 3)
]

HEURISTIC = {
    "home": 7,
    "station": 5,
    "park": 4,
    "library": 2,
    "university": 0
}

def prolog_best_first(current, goal, visited=None):
    if visited is None:
        visited = []
    visited = visited + [current]

    if current == goal:
        return visited

    # Find all neighbors matching edge(current, Next, _)
    neighbors = [to_node for (from_node, to_node, _) in EDGES if from_node == current and to_node not in visited]
    # Sort neighbors by heuristic h(Next, H) ascending
    neighbors.sort(key=lambda node: HEURISTIC[node])

    for next_node in neighbors:
        result = prolog_best_first(next_node, goal, visited)
        if result:
            return result
    return None

if __name__ == "__main__":
    path = prolog_best_first("home", "university")
    print("Prolog-Style Declarative Best-First Route:")
    print(" -> ".join(path))
