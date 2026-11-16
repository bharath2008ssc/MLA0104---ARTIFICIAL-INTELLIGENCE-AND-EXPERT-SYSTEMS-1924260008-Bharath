"""
Experiment 7: Minimax Algorithm
Scenario: A chess-playing AI must determine the best move against an opponent.
Expected Outcome: Select the optimal move through adversarial search.
"""

def minimax(depth, node_index, is_maximizing_player, scores, max_depth):
    # Base case: leaf node (board evaluation score) reached
    if depth == max_depth:
        return scores[node_index]

    if is_maximizing_player:
        best_val = float("-inf")
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, scores, max_depth)
            best_val = max(best_val, val)
        return best_val
    else:
        best_val = float("inf")
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, scores, max_depth)
            best_val = min(best_val, val)
        return best_val

if __name__ == "__main__":
    # Leaf node heuristic board evaluations for possible chess move sequences
    # Depth 3 binary game tree (8 leaf outcomes)
    board_evaluations = [3, 5, 2, 9, 12, 5, 23, 23]
    tree_depth = 3

    left_move_score = minimax(1, 0, False, board_evaluations, tree_depth)
    right_move_score = minimax(1, 1, False, board_evaluations, tree_depth)
    optimal_score = minimax(0, 0, True, board_evaluations, tree_depth)

    best_move = "Move A (Left Branch)" if left_move_score >= right_move_score else "Move B (Right Branch)"
    print(f"Evaluated Move A Score: {left_move_score}")
    print(f"Evaluated Move B Score: {right_move_score}")
    print(f"Chess AI Optimal Decision: {best_move} with guaranteed score {optimal_score}")
