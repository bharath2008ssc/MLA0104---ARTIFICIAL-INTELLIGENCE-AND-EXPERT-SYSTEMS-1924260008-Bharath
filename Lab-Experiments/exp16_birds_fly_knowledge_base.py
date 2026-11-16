"""
Experiment 16: Birds Fly Knowledge Base
Scenario: A wildlife information system determines whether an animal can fly based on its characteristics.
Expected Outcome: Perform inheritance-based reasoning.
"""

class AnimalNode:
    def __init__(self, name, parent=None, properties=None):
        self.name = name
        self.parent = parent
        self.properties = properties or {}

    def query(self, attribute):
        # Inheritance lookup with exception overriding
        if attribute in self.properties:
            return self.properties[attribute]
        if self.parent is not None:
            return self.parent.query(attribute)
        return None

if __name__ == "__main__":
    animal = AnimalNode("Animal", properties={"moves": True})
    bird = AnimalNode("Bird", parent=animal, properties={"has_feathers": True, "can_fly": True})
    flightless_bird = AnimalNode("Flightless_Bird", parent=bird, properties={"can_fly": False})

    sparrow = AnimalNode("Sparrow", parent=bird)
    penguin = AnimalNode("Penguin", parent=flightless_bird, properties={"can_swim": True})
    ostrich = AnimalNode("Ostrich", parent=flightless_bird)

    for species in [sparrow, penguin, ostrich]:
        print(f"{species.name}: Has Feathers = {species.query('has_feathers')}, Can Fly = {species.query('can_fly')}")
