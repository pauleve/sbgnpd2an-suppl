class StateVariable:

    def __init__(self, id = None, variable = None, value = None):
        self.id = id
        self.variable = variable
        self.value = value

    def getId(self):
        return self.id
    def getVariable(self):
        return self.variable

    def getValue(self):
        return self.value

    def setVariable(self, var):
        self.variable = var

    def setValue(self, val):
        self.value = val

    def setId(self, id):
        self.id = id
    def __eq__(self, other):
        return isinstance(other, StateVariable) and \
                self.variable == other.variable and \
                self.value == other.value

    def __hash__(self):
        return hash((self.variable, self.value))

    def __str__(self):
        return "id: {0}, {1}@{2}".format(self.id, self.value, self.variable)
