"""
Experiment 9: Water Jug Problem
Scenario: A person has two containers of different capacities and must measure an exact quantity of water.
Expected Outcome: Generate the sequence of operations to reach the goal state.
"""

from collections import deque

def solve_water_jug(cap1, cap2, target):
    visited = set()
    # Queue stores ((jug1, jug2), list_of_steps)
    queue = deque([((0, 0), ["Initial State: (0, 0)"])])
    visited.add((0, 0))

    while queue:
        (j1, j2), steps = queue.popleft()

        if j1 == target or j2 == target:
            return steps

        # Possible operations
        transitions = [
            ((cap1, j2), f"Fill Jug 1 ({cap1}L) -> ({cap1}, {j2})"),
            ((j1, cap2), f"Fill Jug 2 ({cap2}L) -> ({j1}, {cap2})"),
            ((0, j2), f"Empty Jug 1 -> (0, {j2})"),
            ((j1, 0), f"Empty Jug 2 -> ({j1}, 0)"),
            # Pour Jug 1 -> Jug 2
            ((j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),
             f"Pour Jug 1 into Jug 2 -> ({j1 - min(j1, cap2 - j2)}, {j2 + min(j1, cap2 - j2)})"),
            # Pour Jug 2 -> Jug 1
            ((j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1)),
             f"Pour Jug 2 into Jug 1 -> ({j1 + min(j2, cap1 - j1)}, {j2 - min(j2, cap1 - j1)})")
        ]

        for next_state, action_desc in transitions:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, steps + [action_desc]))

    return ["No solution possible."]

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target_volume = 2

    print(f"Measuring {target_volume}L using {jug1_capacity}L and {jug2_capacity}L jugs:")
    solution_steps = solve_water_jug(jug1_capacity, jug2_capacity, target_volume)
    for idx, step in enumerate(solution_steps, 1):
        print(f"Step {idx}: {step}")
