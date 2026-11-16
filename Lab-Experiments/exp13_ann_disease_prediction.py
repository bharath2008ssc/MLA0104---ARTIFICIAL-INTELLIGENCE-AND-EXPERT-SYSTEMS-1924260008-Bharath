"""
Experiment 13: Artificial Neural Network (ANN)
Scenario: A hospital predicts whether a patient has a disease using historical medical records.
Expected Outcome: Train and test a neural network model.
"""

import math
import random

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-max(-500, min(500, x))))

def sigmoid_derivative(output):
    return output * (1.0 - output)

class SimpleANN:
    def __init__(self, input_size, hidden_size, lr=0.5):
        random.seed(42)
        self.lr = lr
        self.w_ih = [[random.uniform(-1, 1) for _ in range(hidden_size)] for _ in range(input_size)]
        self.b_h = [0.0] * hidden_size
        self.w_ho = [random.uniform(-1, 1) for _ in range(hidden_size)]
        self.b_o = 0.0

    def forward(self, x):
        self.hidden = [
            sigmoid(sum(x[i] * self.w_ih[i][h] for i in range(len(x))) + self.b_h[h])
            for h in range(len(self.b_h))
        ]
        self.output = sigmoid(sum(self.hidden[h] * self.w_ho[h] for h in range(len(self.hidden))) + self.b_o)
        return self.output

    def train(self, X, y, epochs=2000):
        for _ in range(epochs):
            for x_sample, target in zip(X, y):
                out = self.forward(x_sample)
                error_o = target - out
                delta_o = error_o * sigmoid_derivative(out)

                deltas_h = [
                    delta_o * self.w_ho[h] * sigmoid_derivative(self.hidden[h])
                    for h in range(len(self.hidden))
                ]

                for h in range(len(self.hidden)):
                    self.w_ho[h] += self.lr * delta_o * self.hidden[h]
                self.b_o += self.lr * delta_o

                for i in range(len(x_sample)):
                    for h in range(len(self.hidden)):
                        self.w_ih[i][h] += self.lr * deltas_h[h] * x_sample[i]
                for h in range(len(self.hidden)):
                    self.b_h[h] += self.lr * deltas_h[h]

if __name__ == "__main__":
    # Normalized Patient Features: [Age_Norm, Blood_Pressure_Norm, Glucose_Norm]
    # Target: 1 = Disease Positive, 0 = Healthy
    X_train = [
        [0.25, 0.30, 0.25],
        [0.30, 0.35, 0.30],
        [0.75, 0.85, 0.90],
        [0.80, 0.80, 0.85],
        [0.45, 0.40, 0.35],
        [0.70, 0.75, 0.80]
    ]
    y_train = [0, 0, 1, 1, 0, 1]

    ann = SimpleANN(input_size=3, hidden_size=4, lr=0.5)
    ann.train(X_train, y_train, epochs=3000)

    test_patients = [
        ([0.28, 0.32, 0.27], "Low-Risk Patient"),
        ([0.78, 0.82, 0.88], "High-Risk Patient")
    ]

    print("--- Hospital ANN Disease Prediction Results ---")
    for features, label in test_patients:
        prob = ann.forward(features)
        diagnosis = "Disease Detected" if prob >= 0.5 else "Healthy"
        print(f"{label} {features} -> Probability: {prob:.4f} | Prediction: {diagnosis}")
