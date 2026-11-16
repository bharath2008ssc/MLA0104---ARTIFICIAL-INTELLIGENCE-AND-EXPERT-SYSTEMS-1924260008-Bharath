"""
Experiment 10: Towers of Hanoi Problem
Scenario: A robotic arm transfers stacked containers while following movement constraints.
Expected Outcome: Generate the optimal sequence of moves.
"""

def towers_of_hanoi(n, source_peg, auxiliary_peg, target_peg, moves=None):
    if moves is None:
        moves = []

    if n == 1:
        moves.append(f"Move Container 1 from {source_peg} -> {target_peg}")
        return moves

    towers_of_hanoi(n - 1, source_peg, target_peg, auxiliary_peg, moves)
    moves.append(f"Move Container {n} from {source_peg} -> {target_peg}")
    towers_of_hanoi(n - 1, auxiliary_peg, source_peg, target_peg, moves)
    return moves

if __name__ == "__main__":
    num_containers = 3
    sequence = towers_of_hanoi(num_containers, "Dock_A", "Buffer_B", "Target_C")
    print(f"Optimal Robotic Arm Sequence for {num_containers} Containers ({len(sequence)} moves):")
    for step_num, move in enumerate(sequence, 1):
        print(f"{step_num}. {move}")
