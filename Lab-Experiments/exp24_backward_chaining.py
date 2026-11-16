"""
Experiment 24: Backward Chaining
Scenario: A medical diagnosis system determines the possible disease by working backward from symptoms.
Expected Outcome: Reach conclusions through goal-driven reasoning.
"""

def backward_chaining(goal, rules, known_facts, visited=None):
    if visited is None:
        visited = set()

    if goal in known_facts:
        return True
    if goal in visited:
        return False
    visited.add(goal)

    for conditions, conclusion in rules:
        if conclusion == goal:
            if all(backward_chaining(cond, rules, known_facts, visited) for cond in conditions):
                return True
    return False

if __name__ == "__main__":
    medical_rules = [
        ({"fever", "cough"}, "respiratory_infection"),
        ({"respiratory_infection", "loss_of_taste"}, "covid_19_suspected"),
        ({"respiratory_infection", "chest_pain"}, "pneumonia_suspected")
    ]

    patient_facts = {"fever", "cough", "loss_of_taste"}

    for hypothesis in ["covid_19_suspected", "pneumonia_suspected"]:
        proven = backward_chaining(hypothesis, medical_rules, patient_facts)
        print(f"Hypothesis '{hypothesis}' proven from facts? -> {proven}")
