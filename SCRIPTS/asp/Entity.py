from EntityClazz import *

class Entity:
    def __init__(self, id = None, clazz = None, label = None, compartmentRef = None, components = None, svs = None):
        self.id = id
        self.clazz = clazz
        self.label = label
        self.compartmentRef = compartmentRef
        if components is not None:
            self.components = components
        else:
            self.components = set()
        if svs is not None:
            self.svs = svs
        else:
            self.svs = set()

    def setId(self, id):
        self.id = id

    def setClazz(self, clazz):
        self.clazz = clazz

    def setLabel(self, label):
        self.label = label

    def setCompartmentRef(self, compartmentRef):
        self.compartmentRef = compartmentRef

    def setComponents(self, components):
        self.components = components

    def addComponent(self, component):
        self.components.add(component)

    def removeComponent(self, component):
        self.components.remove(component)

    def setStateVariables(self, svs):
        self.svs = svs

    def addStateVariable(self, sv):
        self.svs.add(sv)

    def removeStateVariable(self, sv):
        self.svs.remove(sv)

    def getId(self):
        return self.id

    def getClazz(self):
        return self.clazz

    def getLabel(self):
        return self.label

    def getCompartmentRef(self):
        return self.compartmentRef

    def getComponents(self):
        return self.components

    def getStateVariables(self):
        return self.svs

    def hasLabel(self):
        return self.label is not None

    def __eq__(self, other):
        if not isinstance(other, Entity):
            return False
        if not self.clazz == EntityClazz.SOURCE_AND_SINK:
            return self.label == other.label and \
                self.clazz == other.clazz and \
                self.compartmentRef == other.compartmentRef and \
                self.components == other.components and \
                self.svs == other.svs
        else:
            return self.id == other.id and self.clazz == other.clazz

    def __hash__(self):
        if not self.clazz == EntityClazz.SOURCE_AND_SINK:
            return hash((self.clazz, self.label, self.compartmentRef, frozenset(self.components), frozenset(self.svs)))
            # return [0, hash(self.clazz)][self.clazz is not None] + \
            #         [0, hash(self.label)][self.label is not None] + \
            #         [0, hash(self.compartmentRef)][self.compartmentRef is not None] + \
            #         [0, hash(frozenset(self.components))][len(self.components) > 0] + \
            #         [0, hash(frozenset(self.svs))][len(self.svs) > 0]
        else:
            return hash(self.id)


    def __str__(self):
        s = "id: {0}, clazz: {1}, label: {2}\n".format(self.getId(), self.getClazz(), self.getLabel())
        for sv in self.getStateVariables():
            s += "  Sv:{0}\n".format(sv)
        return s

