"""
Experiment 26: Sum of 1 to N using Recursion
Scenario: A mathematical tutoring system computes the sum of natural numbers recursively.
Expected Outcome: Demonstrate recursive problem solving.
"""

def recursive_sum(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)

if __name__ == "__main__":
    n = 10
    total = recursive_sum(n)
    print(f"Mathematical Tutoring System: Sum of natural numbers from 1 to {n} = {total}")
