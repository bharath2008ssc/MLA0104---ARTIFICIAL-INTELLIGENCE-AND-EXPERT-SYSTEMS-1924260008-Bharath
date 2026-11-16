"""
Experiment 22: Monkey and Banana Problem
Scenario: A robot must retrieve food placed on a high shelf by planning a sequence of actions.
Expected Outcome: Generate an optimal action plan.
"""

from collections import deque

def solve_monkey_banana():
    # State: (monkey_pos, box_pos, monkey_on_box, has_banana)
    initial_state = ("Door", "Window", False, False)
    positions = ["Door", "Window", "Center"]

    queue = deque([(initial_state, [])])
    visited = {initial_state}

    while queue:
        (m_pos, b_pos, on_box, has_banana), plan = queue.popleft()

        if has_banana:
            return plan

        possible_actions = []

        # Action 1: Walk to another position (if not on box)
        if not on_box:
            for pos in positions:
                if pos != m_pos:
                    possible_actions.append(
                        ((pos, b_pos, False, has_banana), f"Walk from {m_pos} to {pos}")
                    )

        # Action 2: Push box to another position (if at same position and not on box)
        if not on_box and m_pos == b_pos:
            for pos in positions:
                if pos != m_pos:
                    possible_actions.append(
                        ((pos, pos, False, has_banana), f"Push box from {m_pos} to {pos}")
                    )

        # Action 3: Climb onto box
        if not on_box and m_pos == b_pos:
            possible_actions.append(
                ((m_pos, b_pos, True, has_banana), f"Climb onto box at {m_pos}")
            )

        # Action 4: Grasp banana (if on box at Center under shelf)
        if on_box and m_pos == "Center":
            possible_actions.append(
                ((m_pos, b_pos, True, True), "Grasp banana from high shelf")
            )

        for next_state, action_name in possible_actions:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, plan + [action_name]))

    return []

if __name__ == "__main__":
    optimal_plan = solve_monkey_banana()
    print("--- Optimal Action Plan (Monkey & Banana / Shelf Robot) ---")
    for idx, step in enumerate(optimal_plan, 1):
        print(f"Step {idx}: {step}")
