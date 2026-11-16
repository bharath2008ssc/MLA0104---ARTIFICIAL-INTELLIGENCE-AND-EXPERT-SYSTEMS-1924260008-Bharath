"""
Experiment 18: Fruit Color Classification
Scenario: A fruit-sorting machine identifies fruits based on their colors.
Expected Outcome: Classify fruits using production rules.
"""

PRODUCTION_RULES = [
    ({"color": "red", "shape": "round"}, "Apple"),
    ({"color": "yellow", "shape": "curved"}, "Banana"),
    ({"color": "orange", "shape": "round"}, "Orange"),
    ({"color": "purple", "shape": "cluster"}, "Grapes"),
    ({"color": "green", "shape": "oval"}, "Watermelon")
]

def classify_fruit(color, shape):
    facts = {"color": color.lower(), "shape": shape.lower()}
    for conditions, fruit_name in PRODUCTION_RULES:
        if all(facts.get(k) == v for k, v in conditions.items()):
            return fruit_name
    return "Unknown Fruit"

if __name__ == "__main__":
    conveyor_items = [
        ("Red", "Round"),
        ("Yellow", "Curved"),
        ("Purple", "Cluster"),
        ("Orange", "Round")
    ]

    print("--- Automated Fruit-Sorting Machine Output ---")
    for color, shape in conveyor_items:
        print(f"Sensor Input [Color={color}, Shape={shape}] -> Classified as: {classify_fruit(color, shape)}")
