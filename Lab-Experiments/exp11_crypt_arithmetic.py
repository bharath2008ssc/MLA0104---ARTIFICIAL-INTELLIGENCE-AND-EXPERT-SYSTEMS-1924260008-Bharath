"""
Experiment 11: Crypt Arithmetic Problem
Scenario: A banking application verifies encrypted arithmetic puzzles before processing transactions.
Expected Outcome: Assign valid digits satisfying arithmetic constraints.
Puzzle: SEND + MORE = MONEY
"""

import itertools

def solve_cryptarithmetic():
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading digits cannot be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        send = mapping['S'] * 1000 + mapping['E'] * 100 + mapping['N'] * 10 + mapping['D']
        more = mapping['M'] * 1000 + mapping['O'] * 100 + mapping['R'] * 10 + mapping['E']
        money = (mapping['M'] * 10000 + mapping['O'] * 1000 +
                 mapping['N'] * 100 + mapping['E'] * 10 + mapping['Y'])

        if send + more == money:
            return mapping, send, more, money

    return None

if __name__ == "__main__":
    result = solve_cryptarithmetic()
    if result:
        mapping, send, more, money = result
        print("Banking Encrypted Verification Solved (SEND + MORE = MONEY):")
        print("Digit Mapping:", mapping)
        print(f"Verification: {send} + {more} = {money}")
    else:
        print("No valid digit assignment found.")
