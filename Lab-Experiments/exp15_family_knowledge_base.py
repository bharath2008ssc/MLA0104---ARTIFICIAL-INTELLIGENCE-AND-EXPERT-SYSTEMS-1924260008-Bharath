"""
Experiment 15: Family Knowledge Representation
Scenario: A genealogy application determines relationships among family members.
Expected Outcome: Infer family relationships using logical rules.
"""

class FamilyKB:
    def __init__(self):
        self.parents = []  # (parent, child)
        self.male = set()
        self.female = set()

    def add_parent(self, parent, child):
        self.parents.append((parent, child))

    def is_father(self, x, y):
        return (x, y) in self.parents and x in self.male

    def is_mother(self, x, y):
        return (x, y) in self.parents and x in self.female

    def is_sibling(self, x, y):
        if x == y:
            return False
        return any((p, x) in self.parents and (p, y) in self.parents for p, _ in self.parents)

    def is_grandparent(self, x, z):
        return any((x, y) in self.parents and (y, z) in self.parents for _, y in self.parents)

    def is_uncle_or_aunt(self, x, z):
        return any((p, z) in self.parents and self.is_sibling(x, p) for p, _ in self.parents)

if __name__ == "__main__":
    kb = FamilyKB()
    kb.male.update(["Arthur", "Charles", "William", "Harry"])
    kb.female.update(["Elizabeth", "Diana"])

    kb.add_parent("Elizabeth", "Charles")
    kb.add_parent("Elizabeth", "Anne")
    kb.add_parent("Charles", "William")
    kb.add_parent("Charles", "Harry")
    kb.add_parent("Diana", "William")
    kb.add_parent("Diana", "Harry")

    print("Is Elizabeth grandparent of William?", kb.is_grandparent("Elizabeth", "William"))
    print("Is William sibling of Harry?", kb.is_sibling("William", "Harry"))
    print("Is Anne aunt/uncle of Harry?", kb.is_uncle_or_aunt("Anne", "Harry"))
