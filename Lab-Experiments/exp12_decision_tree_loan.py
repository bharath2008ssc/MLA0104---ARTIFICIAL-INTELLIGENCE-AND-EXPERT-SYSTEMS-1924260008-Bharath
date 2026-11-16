"""
Experiment 12: Decision Tree Classifier
Scenario: A bank wants to approve or reject loan applications based on customer information.
Expected Outcome: Classify data using decision tree learning.
"""

import math

# Pure-Python ID3 Decision Tree implementation (also works without external libraries)
def entropy(rows):
    counts = {}
    for row in rows:
        label = row[-1]
        counts[label] = counts.get(label, 0) + 1
    ent = 0.0
    for count in counts.values():
        p = count / len(rows)
        ent -= p * math.log2(p)
    return ent

def info_gain(rows, col_idx):
    base_ent = entropy(rows)
    subsets = {}
    for row in rows:
        subsets.setdefault(row[col_idx], []).append(row)
    weighted_ent = sum((len(sub) / len(rows)) * entropy(sub) for sub in subsets.values())
    return base_ent - weighted_ent

def build_tree(rows, headers):
    labels = [row[-1] for row in rows]
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    if len(headers) == 1:
        return max(set(labels), key=labels.count)

    gains = [info_gain(rows, i) for i in range(len(headers) - 1)]
    best_col = gains.index(max(gains))
    best_feature = headers[best_col]

    tree = {best_feature: {}}
    feature_values = set(row[best_col] for row in rows)
    for val in feature_values:
        sub_rows = [row[:best_col] + row[best_col + 1:] for row in rows if row[best_col] == val]
        sub_headers = headers[:best_col] + headers[best_col + 1:]
        tree[best_feature][val] = build_tree(sub_rows, sub_headers)
    return tree

def predict(tree, headers, sample):
    if not isinstance(tree, dict):
        return tree
    feature = next(iter(tree))
    idx = headers.index(feature)
    val = sample[idx]
    branch = tree[feature].get(val, "Reject")
    return predict(branch, headers, sample)

if __name__ == "__main__":
    headers = ["Credit_Score", "Income_Level", "Existing_Debt", "Loan_Status"]
    dataset = [
        ["High", "High", "No", "Approve"],
        ["High", "Medium", "No", "Approve"],
        ["High", "Low", "Yes", "Reject"],
        ["Medium", "High", "No", "Approve"],
        ["Medium", "Medium", "Yes", "Reject"],
        ["Low", "High", "No", "Reject"],
        ["Low", "Low", "Yes", "Reject"],
        ["Medium", "High", "Yes", "Approve"]
    ]

    decision_tree = build_tree(dataset, headers)
    print("Trained Loan Decision Tree:", decision_tree)

    new_applicant = ["Medium", "High", "No"]
    decision = predict(decision_tree, headers[:-1], new_applicant)
    print(f"Applicant {dict(zip(headers[:-1], new_applicant))} -> Loan Decision: {decision}")
