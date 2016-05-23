from ProcessClazz import *

class Process:

    def __init__(self, id = None, clazz = None, label = None, reactants = None, products = None):
        self.id = id
        self.clazz = clazz
        self.label = label
        if reactants is not None:
            self.reactants = reactants
        else:
            self.reactants = set()
        if products is not None:
            self.products = products
        else:
            self.products = set()

    def getId(self):
        return self.id

    def getClazz(self):
        return self.clazz

    def getLabel(self):
        return self.label

    def getReactants(self):
        return self.reactants

    def getProducts(self):
        return self.products

    def setId(self, id):
        self.id = id

    def setClazz(self, clazz):
        self.clazz = clazz

    def setLabel(self, label):
        self.label = label

    def setReactants(self, reactants):
        self.reactants = reactants

    def setProducts(self, products):
        self.products = products

    def addReactant(self, reactant):
        self.reactants.add(reactant)

    def addProduct(self, product):
        self.products.add(product)

    def __eq__(self, other):
        return isinstance(other, Process) and \
                self.clazz == other.clazz and \
                self.label == other.label and \
                self.reactants == other.reactants and \
                self.products == other.products

    def __hash__(self):
        return hash((self.clazz, self.label, frozenset(self.reactants), frozenset(self.products)))
        # return [0, hash(self.clazz)][self.clazz is not None] + \
        #         [0, hash(self.label)][self.label is not None] + \
        #         [0, hash(frozenset(self.reactants))][len(self.reactants) > 0] + \
        #         [0, hash(frozenset(self.products))][len(self.products) > 0]

    def __str__(self):
        s = "id: {0}, clazz: {1}, label: {2}\n".format(self.id, self.clazz, self.label)
        for reac in self.reactants:
            s += "  Reactant: {0}\n".format(reac)
        for prod in self.products:
            s += "  Product: {0}\n".format(prod)
        return s
