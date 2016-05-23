import libsbgnpy.libsbgn as libsbgn
from PDNetwork import *
from EntityClazz import *
from ProcessClazz import *
from ModulationClazz import *
from SubEntityClazz import *
from StateVariable import *
# from libsbgnpy.libsbgnTypes import *

class SBGN:

    @staticmethod
    def makeSvFromGlyph(sbgnMap, net, glyph):
        if glyph.get_state() is not None:
            return StateVariable(glyph.get_id(), glyph.get_state().get_variable(), glyph.get_state().get_value())
        else:
            return StateVariable()

    @staticmethod
    def makeEntityFromGlyph(sbgnMap, net, glyph):
        entity = Entity()
        entity.setId(glyph.get_id())
        entity.setClazz(EntityClazz[glyph.get_class().name])
        if glyph.get_label() is not None:
            entity.setLabel(glyph.get_label().get_text())
        else:
            entity.setLabel(None)
        entity.setCompartmentRef(glyph.get_compartmentRef())
        for subglyph in glyph.get_glyph():
            if subglyph.get_class().name in [attribute.name for attribute in list(EntityClazz)]:
                subentity = SBGN.makeEntityFromGlyph(sbgnMap, net, subglyph)
                entity.addComponent(subentity)
            elif subglyph.get_class().name == 'STATE_VARIABLE':
                sv = SBGN.makeSvFromGlyph(sbgnMap, net, subglyph)
                entity.addStateVariable(sv)
        already = net.getEntity(entity)
        if already is not None:
            return already
        else:
            return entity

    @staticmethod
    def getGlyphById(sbgnMap, id):
        for glyph in sbgnMap.get_glyph():
            if glyph.get_id() == id:
                return glyph
        return None

    @staticmethod
    def makeProcessFromGlyph(sbgnMap, net, glyph):
        process = Process()
        process.setId(glyph.get_id())
        process.setClazz(ProcessClazz[glyph.get_class().name])
        if glyph.get_label() is not None:
            process.setLabel(glyph.get_label().get_text())
        else:
            process.setLabel(None)
        for arc in sbgnMap.get_arc():
            if arc.get_class().name == "CONSUMPTION" and arc.get_target() in [port.get_id() for port in glyph.get_port()]:
                sourceId = arc.get_source()
                sourceGlyph = SBGN.getGlyphById(sbgnMap, sourceId)
                sourceEntity = SBGN.makeEntityFromGlyph(sbgnMap, net, sourceGlyph)
                reactant = net.getEntity(sourceEntity)
                process.addReactant(reactant)
            elif arc.get_class().name == "PRODUCTION" and arc.get_source() in [port.get_id() for port in glyph.get_port()]:
                targetId = arc.get_target()
                targetGlyph = SBGN.getGlyphById(sbgnMap, targetId)
                targetEntity = SBGN.makeEntityFromGlyph(sbgnMap, net, targetGlyph)
                product = net.getEntity(targetEntity)
                process.addProduct(product)
        already = net.getProcess(process)
        if already is not None:
            return already
        else:
            return process

    @staticmethod
    def makeModulationFromArc(sbgnMap, net, arc):
        sourceId = arc.get_source()
        sourceGlyph = SBGN.getGlyphById(sbgnMap, sourceId)
        sourceEntity = SBGN.makeEntityFromGlyph(sbgnMap, net, sourceGlyph)
        sourceEntity = net.getEntity(sourceEntity)
        targetId = arc.get_target()
        targetGlyph = SBGN.getGlyphById(sbgnMap, targetId)
        targetProcess = SBGN.makeProcessFromGlyph(sbgnMap, net, targetGlyph)
        targetProcess = net.getProcess(targetProcess)
        clazz = ModulationClazz[arc.get_class().name]
        modulation = Modulation(clazz, sourceEntity, targetProcess)
        return modulation

    @staticmethod
    def readSBGNML(filename):
        sbgn = libsbgn.parse(filename, silence=True)
        sbgnMap = sbgn.get_map()
        net = PDNetwork()
        for glyph in sbgnMap.get_glyph():
            if glyph.get_class().name in [attribute.name for attribute in list(EntityClazz)]:
                entity  = SBGN.makeEntityFromGlyph(sbgnMap, net, glyph)
                net.addEntity(entity)
        for glyph in sbgnMap.get_glyph():
            if glyph.get_class().name in [attribute.name for attribute in list(ProcessClazz)]:
                process = SBGN.makeProcessFromGlyph(sbgnMap, net, glyph)
                net.addProcess(process)
        # Bug modulations with logical operators with ports that can be source
        for arc in sbgnMap.get_arc():
            if arc.get_class().name in [attribute.name for attribute in list(ModulationClazz)]:
                modulation = SBGN.makeModulationFromArc(sbgnMap, net, arc)
                net.addModulation(modulation)
        return net

    @staticmethod
    def getCG2ASP(net):
        s = ""
        for entity in net.getEntities():
            if not net.isSink(entity):
                s += "epn({0}).\n".format(entity.getId())
                if entity.hasLabel():
                    s += "belong({0}, {1}).\n".format(SBGN.normalizeLabel(entity.getLabel()), entity.getId())
                for subentity in entity.getComponents():
                    if subentity.hasLabel():
                        s += "belong({0}, {1}).\n".format(SBGN.normalizeLabel(subentity.getLabel()), entity.getId())
        for process in net.getProcesses():
            reactants = process.getReactants()
            products = process.getProducts()
            if len(reactants) == 0:
                for product in products:
                    for product2 in products:
                        if product != product2:
                            if not net.isSink(product):
                                s += "edge({0},{1},{2}).\n".format(product.getId(), product2.getId(), process.getId())
            else:
                for reactant in reactants:
                    for product in products:
                        if not net.isSink(product):
                            s += "edge({0},{1},{2}).\n".format(reactant.getId(), product.getId(), process.getId())
        return s

    @staticmethod
    def writeCG2ASP(net, filename):
        ofile = open(filename, "w")
        s = SBGN.getCG2ASP(net)
        ofile.write(s)
        ofile.close()

    @staticmethod
    def normalizeLabel(label):
        label = label.replace("*","_")
        label = label.replace("/","_")
        label = label.replace(" ","_")
        label = label.replace("-","_")
        label = label.lower()
        return label

    @staticmethod
    def writeSBGNML(net, filename):
        sbgn = SBGN.makeSBGNML(net)
        sbgn.write_file(filename)
        ifile = open(filename)
        s = ifile.read()
        ifile.close()
        s = s.replace("sbgn:","")
        s = s.replace(' xmlns:sbgn="http://sbgn.org/libsbgn/0.2"', "")
        s = s.replace('."', '.0"')
        ofile = open(filename, "w")
        ofile.write(s)
        ofile.close()


    @staticmethod
    def makeGlyphFromEntity(epn, iglyph):
        g = libsbgn.glyph()
        g.set_class(libsbgn.GlyphClass[epn.getClazz().name])
        g.set_id("glyph{0}".format(iglyph))
        iglyph += 1
        bbox = libsbgn.bbox(0, 0, epn.getClazz().value["w"], epn.getClazz().value["h"])
        g.set_bbox(bbox)
        label = libsbgn.label()
        label.set_text(epn.getLabel())
        g.set_label(label)
        for component in epn.getComponents():
            iglyph, gc = SBGN.makeGlyphFromComponent(component, iglyph)
            g.add_glyph(gc)
        for i, sv in enumerate(epn.getStateVariables()):
            gsv = libsbgn.glyph()
            gsv.set_id("glyph{0}".format(iglyph))
            iglyph += 1
            gsv.set_class(libsbgn.GlyphClass["STATE_VARIABLE"])
            gsv.set_state(libsbgn.stateType(sv.getVariable(), sv.getValue()))
            bbox = libsbgn.bbox()
            bbox.set_x(g.get_bbox().get_x()+40*i+6)
            bbox.set_y(g.get_bbox().get_y()-10)
            bbox.set_h(22)
            bbox.set_w(40)
            gsv.set_bbox(bbox)
            g.add_glyph(gsv)
        return iglyph, g

    def makeGlyphFromComponent(comp, iglyph):
        g = libsbgn.glyph()
        g.set_class(libsbgn.GlyphClass[comp.getClazz().name])
        g.set_id("glyph{0}".format(iglyph))
        iglyph += 1
        bbox = libsbgn.bbox(0, 0, comp.getClazz().value["w"], comp.getClazz().value["h"])
        g.set_bbox(bbox)
        label = libsbgn.label()
        label.set_text(comp.getLabel())
        g.set_label(label)
        for component in comp.getComponents():
            iglyph, gc = SBGN.makeGlyphFromComponent(component, iglyph)
            g.add_glyph(gc)
        for i, sv in enumerate(comp.getStateVariables()):
            gsv = libsbgn.glyph()
            gsv.set_id("glyph{0}".format(iglyph))
            iglyph += 1
            gsv.set_class(libsbgn.GlyphClass["STATE_VARIABLE"])
            gsv.set_state(libsbgn.stateType(sv.getVariable(), sv.getValue()))
            bbox = libsbgn.bbox()
            bbox.set_x(g.get_bbox().get_x()+40*i+6)
            bbox.set_y(g.get_bbox().get_y()-10)
            bbox.set_h(22)
            bbox.set_w(40)
            gsv.set_bbox(bbox)
            g.add_glyph(gsv)
        return iglyph, g


    @staticmethod
    def makeGlyphFromProcess(process, iglyph):
        p = libsbgn.glyph()
        p.set_class(libsbgn.GlyphClass[process.getClazz().name])
        p.set_id("glyph{0}".format(iglyph))
        iglyph += 1
        bbox = libsbgn.bbox(0, 0, process.getClazz().value["w"], process.getClazz().value["h"])
        p.set_bbox(bbox)
        port1 = libsbgn.port()
        # port1.set_id("{0}.1".format(p.get_id()))
        # port1.set_y(bbox.get_y() + bbox.get_h() / 2)
        # port1.set_x(bbox.get_x())
        # port2 = libsbgn.port()
        # port2.set_id("{0}.2".format(p.get_id()))
        # port2.set_y(bbox.get_y() + bbox.get_h() / 2)
        # port2.set_x(bbox.get_x() + bbox.get_w())
        # p.add_port(port1)
        # p.add_port(port2)
        return iglyph, p

    @staticmethod
    def makeArcsFromProcess(process, iarc, dids):
        arcs = []
        for reactant in process.getReactants():
            arc = libsbgn.arc()
            start = libsbgn.startType(0, 0)
            end = libsbgn.endType(0, 0)
            arc.set_source(dids[reactant.getId()])
            # arc.set_target("{0}.1".format(process.getId()))
            arc.set_target(dids[process.getId()])
            arc.set_id("arc{0}".format(iarc))
            iarc += 1
            arc.set_start(start)
            arc.set_end(end)
            arc.set_class(libsbgn.ArcClass.CONSUMPTION)
            arcs.append(arc)
        for product in process.getProducts():
            arc = libsbgn.arc()
            start = libsbgn.startType(0, 0)
            end = libsbgn.endType(0, 0)
            # arc.set_source("{0}.2".format(process.getId()))
            arc.set_source(dids[process.getId()])
            arc.set_target(dids[product.getId()])
            arc.set_id("arc{0}".format(iarc))
            iarc += 1
            arc.set_start(start)
            arc.set_end(end)
            arc.set_class(libsbgn.ArcClass.PRODUCTION)
            arcs.append(arc)
        return iarc, arcs

    @staticmethod
    def makeArcFromModulation(modulation, iarc, dids):
        arc = libsbgn.arc()
        start = libsbgn.startType(0, 0)
        end = libsbgn.endType(0, 0)
        arc.set_source(dids[modulation.getSource().getId()])
        arc.set_target(dids[modulation.getTarget().getId()])
        arc.set_id("arc{0}".format(iarc))
        iarc += 1
        arc.set_start(start)
        arc.set_end(end)
        arc.set_class(libsbgn.ArcClass[modulation.getClazz().name])
        return iarc, arc

    @staticmethod
    def makeSBGNML(net):
        iglyph = 0
        iarc = 0
        sbgn = libsbgn.sbgn()
        sbgnmap = libsbgn.map()
        language = libsbgn.Language.PD
        sbgnmap.set_language(language)
        sbgn.set_map(sbgnmap);
        dids = {}
        for epn in net.getEntities():
            iglyph, g = SBGN.makeGlyphFromEntity(epn, iglyph)
            sbgnmap.add_glyph(g)
            dids[epn.getId()] = g.get_id()
        for process in net.getProcesses():
            iglyph, p = SBGN.makeGlyphFromProcess(process, iglyph)
            sbgnmap.add_glyph(p)
            dids[process.getId()] = p.get_id()
            iarc, arcs = SBGN.makeArcsFromProcess(process, iarc, dids)
            for arc in arcs:
                sbgnmap.add_arc(arc)
        for modulation in net.getModulations():
            iarc, arc = SBGN.makeArcFromModulation(modulation, iarc, dids)
            sbgnmap.add_arc(arc)
        return sbgn

if __name__ == "__main__":
    net = SBGN.readSBGNML("example.sbgn")
    SBGN.writeSBGNML(net, "example2.sbgn")
