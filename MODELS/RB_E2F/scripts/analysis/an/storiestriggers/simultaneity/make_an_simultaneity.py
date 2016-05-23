#!/bin/python

from collections import defaultdict

def readPhases(infile):
    dphases = defaultdict(set)
    ifile = open(infile)
    for i, line in enumerate(ifile):
        if i == 0:
            order = line[:-1].split("#")[0].replace(" ","").split(",")
            continue
        if line[0] != "#" and line != "\n":
            l = line.replace(" ","").split("#")[0].split(":")
            phase = l[0]
            if l[1][-1] == '\n':
                l[1] =l[1][:-1]
            conjuncts = frozenset(l[1].split(","))
            dphases[phase].add(conjuncts)
    ifile.close()
    return order, dphases


def stateNoStory(state):
    l = state.split('=')
    if l[1].isdigit():
        return state
    state = l[1] + "=1"
    return state

def stateAN(state):
    state = state.replace('"','')
    l = state.split('=')
    state = '"{0}"'.format(l[0])
    state += "="
    if not l[1].isdigit():
        state += '"{0}"'.format(l[1])
    else:
        state += l[1]
    return state

def statePhase(state):
    return state.replace('"','')

if __name__ == '__main__':
    model = "storiestriggers"
    fphases = "MODELS/RB_E2F/analysis/phases/rb_e2f.phases"
    fmodel = "MODELS/RB_E2F/analysis/an/"+model+".an"
    tempbase = "MODELS/RB_E2F/analysis/an/simultaneity/"+model+"/"
    order, dphases = readPhases(fphases)

    for i, p in enumerate(order):
        for j, q in enumerate(order[i+1:]):
            for c in dphases[order[i]]:
                for s in c:
                    for d in dphases[q]:
                        for r in d:
                            st = ""
                            ifile = open(fmodel)
                            for line in ifile:
                                if "initial_context" in line or "initial_state" in line:
                                    s = stateAN(s)
                                    r = stateAN(r)
                                    st += '"{0}_{1}" [0,1]\n'.format(p, q)
                                    st += '"{0}_{1}" 0 -> 1 when {2} and {3}\n'.format(p, q, s, r)
                                    if line[-1] == '\n':
                                        line = line[:-1]
                                    line += ',"{0}_{1}" = 0\n'.format(p, q)
                                st += line
                            s = statePhase(s)
                            r = statePhase(r)
                            temp = tempbase + model
                            temp += "_"
                            temp += p
                            temp += "_"
                            temp += q
                            temp += "_"
                            temp += s
                            temp += "_"
                            temp += r
                            temp += ".an"
                            ofile = open(temp, "w")
                            ofile.write(st)
                            ofile.close()
