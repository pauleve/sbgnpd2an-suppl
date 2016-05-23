

class Compartment:
    def __init__(self, id = None, label = None):
        self.id = id
        self.label = label

    def getLabel(self):
        return self.label

    def getId(semf):
        return self.id

    def setLabel(self, label):
        self.label = label

    def setId(self, id):
        self.id = id

    def __eq__(self, other):
        return isinstance(other, Compartment) and self.label == other.label

    def __hash__(self):
        return hash(self.label)
