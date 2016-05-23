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

    situations = ["normal","disable_e2f1","disable_prev_phase"]
    models = ["nostories","stories","nostoriestriggers","storiestriggers","storiestriggers2"]
    fphases = "MODELS/RB_E2F/analysis/phases/rb_e2f.phases"
    ofile = open("MODELS/RB_E2F/analysis/results/results.csv", "w")

    order, dphases = readPhases(fphases)
    dresults = {}

    for situation in situations:
        dresults[situation] = {}
        for model in models:
            dresults[situation][model] = {}
            for phase in order:
                all = "False"
                dresults[situation][model][phase] = {}
                for conjunct in dphases[phase]:
                    for state in conjunct:
                        path = "MODELS/RB_E2F/analysis/reach/"
                        path += model
                        path += "/"
                        path += situation
                        path += "/"
                        path += model
                        path += "_"
                        path += phase
                        path += "_"
                        if model == "nostories" or model == "nostoriestriggers":
                            state = state.split("=")[1]+"=1"
                        path += state
                        path += ".reach"
                        res = open(path).read()[:-1]
                        dresults[situation][model][phase][state] = res
                        if res == "True":
                            all = "True"
                dresults[situation][model][phase]["all"] = all


    # ofile.write("phase,state,")
    #
    # for situation in situations:
    #     ofile.write(situation)
    #     for model in models:
    #         ofile.write(",")
    #
    # ofile.write("\n")
    # ofile.write(",,")
    # for situation in situations:
    #     for model in models:
    #         ofile.write(model)
    #         ofile.write(",")
    #
    # ofile.write("\n")
    #
    # for i, phase in enumerate(order):
    #     ofile.write(phase)
    #     for j, conjunct in enumerate(dphases[phase]):
    #         for k, state in enumerate(conjunct):
    #             ofile.write(",")
    #             ofile.write(state)
    #             ofile.write(",")
    #             for situation in situations:
    #                 for model in models:
    #                     if model == "nostories" or model == "nostoriestriggers":
    #                         statebis = state.split("=")[1]+"=1"
    #                     else:
    #                         statebis = state
    #                     ofile.write(dresults[situation][model][phase][statebis])
    #                     ofile.write(",")
    #             ofile.write("\n")
    #

    ofile.write("phase,")

    for situation in situations:
        ofile.write(situation)
        for model in models:
            ofile.write(",")

    ofile.write("\n")
    ofile.write(",")
    for situation in situations:
        for model in models:
            ofile.write(model)
            ofile.write(",")

    ofile.write("\n")
    for phase in order:
        ofile.write(phase)
        ofile.write(",")
        for situation in situations:
            for model in models:
                ofile.write(dresults[situation][model][phase]["all"])
                ofile.write(",")
        ofile.write("\n")

#SIMULTANEITY

    ofile.write("\n\n\n")

    ofile.write("model,")

    for model in models:
        ofile.write("{0}{1}".format(model, ","*len(order)))

    ofile.write("\nphase,")

    for model in models:
        for p in order:
            ofile.write("{0},".format(p))
    ofile.write("\n")

    for i, p in enumerate(order):
    #    print("Phase1 : {0}".format(p))
        st = "{0}:".format(p)
        ofile.write("{0},".format(p))
        for model in models:
    #        print(" Model : {0}".format(model))
            ofile.write(","*(i+1))
            for j, q in enumerate(order[i+1:]):
    #            print("     Phase2 : {0}".format(q))
                all = "False"
                for c in dphases[p]:
                    for s in c:
                        if model == "nostories" or model == "nostoriestriggers":
                            s = stateNoStory(s)
                        for d in dphases[q]:
                            for r in d:
                                if model == "nostories" or model == "nostoriestriggers":
                                    r = stateNoStory(r)
                                path = "MODELS/RB_E2F/analysis/reach/{0}/simultaneity/".format(model)
                                path += model
                                path += "_"
                                path += p
                                path += "_"
                                path += q
                                path += "_"
                                path += s
                                path += "_"
                                path += r
                                path += ".reach"
                                res = open(path).read()[:-1]
                                if "True" in res:
                                    all = "True"
                                    break
                                elif "False" in res:
                                    pass
                                else:
                                    all = "Error"
                            if all == "True":
                                break
                        if all == "True":
                            break
                    if all == "True":
                        break
                ofile.write("{0},".format(all))
        ofile.write("\n")
    ofile.close()


