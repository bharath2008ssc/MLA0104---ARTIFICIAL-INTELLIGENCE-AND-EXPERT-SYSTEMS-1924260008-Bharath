"""
Experiment 8: Alpha-Beta Pruning
Scenario: A game AI needs to make faster decisions by avoiding unnecessary game-tree exploration.
Expected Outcome: Reduce search time while preserving optimal decisions.
"""

nodes_evaluated = 0

def alpha_beta(depth, node_index, is_maximizing, values, alpha, beta, max_depth):
    global nodes_evaluated
    nodes_evaluated += 1

    if depth == max_depth:
        return values[node_index]

    if is_maximizing:
        best = float("-inf")
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Beta cut-off (pruning)
        return best
    else:
        best = float("inf")
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Alpha cut-off (pruning)
        return best

if __name__ == "__main__":
    game_leaf_scores = [3, 5, 6, 9, 1, 2, 0, -1]
    max_depth = 3

    optimal_value = alpha_beta(0, 0, True, game_leaf_scores, float("-inf"), float("inf"), max_depth)
    print(f"Optimal Value using Alpha-Beta Pruning: {optimal_value}")
    print(f"Total Tree Nodes Visited: {nodes_evaluated} (out of 15 total nodes in full tree)")
