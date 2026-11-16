"""
Experiment 19: Planet Knowledge Representation
Scenario: An astronomy application answers questions about planets in the solar system.
Expected Outcome: Retrieve planetary facts using logical inference.
"""

PLANETS_KB = {
    "Mercury": {"type": "Terrestrial", "moons": 0, "rings": False, "order": 1},
    "Venus": {"type": "Terrestrial", "moons": 0, "rings": False, "order": 2},
    "Earth": {"type": "Terrestrial", "moons": 1, "rings": False, "order": 3},
    "Mars": {"type": "Terrestrial", "moons": 2, "rings": False, "order": 4},
    "Jupiter": {"type": "Gas Giant", "moons": 95, "rings": True, "order": 5},
    "Saturn": {"type": "Gas Giant", "moons": 146, "rings": True, "order": 6},
    "Uranus": {"type": "Ice Giant", "moons": 28, "rings": True, "order": 7},
    "Neptune": {"type": "Ice Giant", "moons": 16, "rings": True, "order": 8}
}

def query_planets_with_rings():
    return [p for p, info in PLANETS_KB.items() if info["rings"]]

def query_terrestrial_planets():
    return [p for p, info in PLANETS_KB.items() if info["type"] == "Terrestrial"]

def query_planets_more_moons_than(count):
    return [p for p, info in PLANETS_KB.items() if info["moons"] > count]

if __name__ == "__main__":
    print("Planets with Ring Systems:", query_planets_with_rings())
    print("Terrestrial (Rocky) Planets:", query_terrestrial_planets())
    print("Planets with more than 20 moons:", query_planets_more_moons_than(20))
