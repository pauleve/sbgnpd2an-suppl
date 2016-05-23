from ModulationClazz import *

class Modulation:

    def __init__(self, clazz = None, source = None, target = None):
        self.source = source
        self.target = target
        self.clazz = clazz

    def getClazz(self):
        return self.clazz

    def getSource(self):
        return self.source

    def getTarget(self):
        return self.target

    def setClazz(self, clazz):
        self.clazz = clazz
    def setSource(self, source):
        self.source = source

    def setTarget(self, target):
        self.target = target

    def __eq__(self, other):
        return self.source == other.source and \
                self.target == other.target

    def __hash__(self):
        return hash((self.source, self.target))
