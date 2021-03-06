
import sys

from xml.dom import *
from xml.dom.minidom import parse

ENTITY_CLASSES = [
        "simple chemical",
        "macromolecule",
        "macromolecule multimer",
        "complex",
    ]
PROCESS_CLASSES = [
        "process",
        "association",
        "dissociation",
        "uncertain process",
    ]
LOGIC_CLASSES = [
        "and",
        "or",
        "not",
    ]
EMPTY_CLASSES = [
        "source and sink",
    ]
COMPARTMENT_CLASSES = [
        "compartment",
    ]
IGNORE_CLASSES = [
    ]
SUPPORTED_GLYPHS =  \
    ENTITY_CLASSES + \
    PROCESS_CLASSES + \
    LOGIC_CLASSES + \
    EMPTY_CLASSES + \
    COMPARTMENT_CLASSES + \
    IGNORE_CLASSES

MODIFICATION_ARCS = [
    "production",
    "consumption",
]
MODULATION_ARCS = [
    "catalysis",
    "stimulation",
    "necessary stimulation",
    "inhibition"
]
LOGIC_ARCS = [
    "logic arc",
]
SUPPORTED_ARCS = \
    MODIFICATION_ARCS + \
    MODULATION_ARCS + \
    LOGIC_ARCS


type2abbrv = {
    "simple chemical": "s",
    "macromolecule": "m",
    "macromolecule multimer": "mm",
    "complex": "cplx",
    "source and sink": "void",
    "process": "p",
    "association": "a",
    "dissociation": "d",
    "uncertain process": "up",
}
def get_type_abbrv(t):
    abbrv = type2abbrv[t]
    return abbrv

class SbgnGlyph:
    compartmentRef = None
    compartment = None
    def __init__(self, dom):
        self.dom = dom
        self.id = self.dom.getAttribute("id")
        self.type = self.dom.getAttribute("class")
        self.ports = {}
        for n in self.dom.childNodes:
            if n.nodeName == "port":
                self.ports[n.getAttribute("id")] = self.id
        if self.dom.hasAttribute("compartmentRef"):
            self.compartmentRef = self.dom.getAttribute("compartmentRef")

    def set_compartment(self, cg):
        self.compartment = cg

    def __repr__(self):
        return "%s(%s,%s)" % (self.__class__.__name__,self.type, self.id)
    

def attr_of_glyph(n):
    cls = n.getAttribute("class")
    assert cls in ["state variable", "unit of information"]
    if cls == "state variable":
        e, a = "state", "value"
    else:
        e, a = "label", "text"
    n = n.getElementsByTagName(e)
    if n:
        n = n[0]
        label = n.getAttribute(a) or ""
        if cls == "state variable" and n.hasAttribute("variable"):
            label += "@%s" % n.getAttribute("variable")
        return label
            

class SbgnCompartment(SbgnGlyph):
    def __init__(self, *args):
        SbgnGlyph.__init__(self, *args)
        for n in self.dom.childNodes:
            if n.nodeName == "label":
                self.label = n.getAttribute("text")

class SbgnLogic(SbgnGlyph):
    def __init__(self, *args):
        SbgnGlyph.__init__(self, *args)
        self.inputs = []
    def add_input(self, e):
        self.inputs.append(e)


class SbgnEntity(SbgnGlyph):
    def __init__(self, *args):
        SbgnGlyph.__init__(self, *args)
        self.consumers = []
        self.producers = []

    def __hash__(self):
        return hash(self.name)

    @property
    def name(self):
        return "%s_%s" % (get_type_abbrv(self.type), self.id)

    def is_clone(self):
        return len(self.dom.getElementsByTagName("clone")) > 0
    def is_void(self):
        return self.type in EMPTY_CLASSES

    def register_consumer(self, p):
        self.consumers.append(p)
    def register_producer(self, p):
        self.producers.append(p)


class SbgnMolecule(SbgnEntity):
    def __init__(self, dom):
        SbgnEntity.__init__(self, dom)
        self.attrs = []
        for n in self.dom.childNodes:
            if n.nodeName == "label":
                self.label = n.getAttribute("text")
            elif n.nodeName == "glyph":
                attr = attr_of_glyph(n)
                if attr:
                    self.attrs.append(attr)

    @property
    def name(self):
        name = self.label
        if self.attrs:
            name += "-"+"-".join(self.attrs)
        if self.compartment:
            name += "/%s" % self.compartment.label
        return name


class SbgnComplex(SbgnEntity):
    def __init__(self, dom):
        SbgnEntity.__init__(self, dom)
        self.attrs = []
        self.components = []
        for n in self.dom.childNodes:
            if n.nodeName == "label":
                self.label = n.getAttribute("text")
            elif n.nodeName == "glyph":
                cls = n.getAttribute("class")
                if cls == "complex":
                    self.components.append(SbgnComplex(n))
                elif cls in ENTITY_CLASSES:
                    self.components.append(SbgnMolecule(n))
                else:
                    attr = attr_of_glyph(n)
                    if attr:
                        self.attrs.append(attr)

    @property
    def name(self):
        if self.components:
            name = "c("+":".join([c.name for c in self.components])+")"
        else:
            assert self.label, "Unsupported complex glyph (%s)"%self.dom.toxml()
            name = self.label
        if self.attrs:
            name += "-"+"-".join(self.attrs)
        if self.compartment:
            name += "/%s" % self.compartment.label
        return name



class SbgnProcess(SbgnGlyph):
    def __init__(self, *args):
        SbgnGlyph.__init__(self, *args)
        self.name = "%s_%s" % (get_type_abbrv(self.type), self.id)
        self.productions = []
        self.consumptions = []
        self.modulations = []

    def is_frontier(self):
        return len(self.consumptions) == 0 \
                or len(self.productions) == 0

    def register_production(self, e):
        if not e.is_void():
            self.productions.append(e)
            e.register_producer(self)

    def register_consumption(self, e):
        if not e.is_void():
            self.consumptions.append(e)
            e.register_consumer(self)

    def register_modulation(self, cls, e):
        self.modulations.append((cls, e))



class SbgnPDModel:
    def __init__(self, dom):
        self.dom = dom
        root = self.dom.documentElement
        maps = root.getElementsByTagName("map")
        assert len(maps) == 1
        assert maps[0].getAttribute("language") == "process description"
        self.mainmap = maps[0]

        self.entities = {}
        self.processes = {}
        self.logic = {}
        self.ports = {}
        self.compartments = {}
        self.g2compartments = {}

        for n in self.mainmap.childNodes:
            if n.nodeName == "glyph":
                cls = n.getAttribute("class")
                assert cls in SUPPORTED_GLYPHS, "Unknown glyph class '%s'" % cls
                g = None
                if cls == "complex":
                    g = SbgnComplex(n)
                    r = self.entities
                elif cls in ENTITY_CLASSES:
                    g = SbgnMolecule(n)
                    r = self.entities
                elif cls in EMPTY_CLASSES:
                    g = SbgnEntity(n)
                    r = self.entities
                elif cls in PROCESS_CLASSES:
                    g = SbgnProcess(n)
                    r = self.processes
                elif cls in LOGIC_CLASSES:
                    g = SbgnLogic(n)
                    r = self.logic
                elif cls in COMPARTMENT_CLASSES:
                    g = SbgnCompartment(n)
                    r = self.compartments
                else:
                    assert cls in IGNORE_CLASSES, cls
                if g is not None:
                    r[g.id] = g
                    self.ports.update(g.ports)
                    if g.compartmentRef is not None:
                        g.set_compartment(self.compartments[g.compartmentRef])

            elif n.nodeName == "arc":
                cls = n.getAttribute("class")
                assert cls in SUPPORTED_ARCS, "Unknown arc class '%s'" % cls

                def resolve(id):
                    id = self.resolve_id(id)
                    if id in self.entities:
                        return self.resolve_clone(self.entities[id])
                    elif id in self.processes:
                        return self.processes[id]
                    else:
                        return self.logic[id]

                source = resolve(n.getAttribute("source"))
                target = resolve(n.getAttribute("target"))
                    
                if cls == "production":
                    source.register_production(target)
                elif cls == "consumption":
                    try:
                        target.register_consumption(source)
                    except:
                        print("Error for arc %s: source is %s" % (n.getAttribute("id"), repr(target)), file=sys.stderr)
                        raise
                elif cls in MODULATION_ARCS:
                    target.register_modulation(cls, source)
                elif cls in LOGIC_ARCS:
                    target.add_input(source)
                else:
                    assert False, cls


    def resolve_id(self, gid):
        if gid in self.ports:
            return self.ports[gid]
        return gid

    def resolve_clone(self, ce):
        if ce.is_clone():
            clones = []
            for e in self.entities.values():
                if e.is_clone() and e.name == ce.name:
                    clones.append((e.id, e))
            return min(clones)[1]
        else:
            return ce
                

def parse_sbgn_pd(fd):
    dom = parse(fd)
    return SbgnPDModel(dom)
    


