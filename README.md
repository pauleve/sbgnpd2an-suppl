# sbgnpd2an-suppl
Supplementary material of the BMC Systems Biology paper on SBGN-PD to Automata Networks

## Requirements

- python >= 3 (http://python.org)
- clingo >= 4 (http://sourceforge.net/projects/potassco/files/clingo/)
- libsbgnpy 0.1.2 (https://pypi.python.org/pypi/libsbgnpy)
- Mole (http://www.lsv.ens-cachan.fr/~schwoon/tools/mole/)
- pint (http://loicpauleve.name/pint/)

## Main programs in SCRIPTS/:
* `maps/cd2sbgnml`:      converts a CellDesigner file to a SBGN-ML file using the CellDesignger file and the SBGN-ML file exported from CellDesigner
* `maps/colorcd`:        colors the stories of a SBGN-PD map
* `asp/sbgnpd2asp`:      writes the compound graph of a SBGN-PD map to ASP
* `stories/stories`:     finds all valid sets of stories of an SBGN-PD map
* `sbgnpd2an/sbgnpd2an`: builds an AN model from a SBGN-PD map under the general or the stories semantics


## Usage examples:

asp/sbgnpd2asp
----------------

Get compound graph in ASP:
    
        SCRIPTS/asp/sbgnpd2asp -o MODELS/Example/asp/example.asp MODELS/Example/maps/example.sbgn

stories/stories
----------------

Get maximally valid sets of stories:

        SCRIPTS/stories/stories --max 1 MODELS/Example/asp/example.asp > MODELS/Example/stories/example1.stories

Get final sets of stories:

        SCRIPTS/stories/stories --max 2 MODELS/Example/asp/example.asp > MODELS/Example/stories/example2.stories

Get valid sets of stories maximazing the number of EPN in stories:

        SCRIPTS/stories/stories --max 3 MODELS/Example/asp/example.asp > MODELS/Example/stories/example3.stories

Get final sets of stories inluding a story with EPNs b and c, and one with EPNs adp,atp:

        SCRIPTS/stories/stories --story glyph3,glyph0 --story glyph8,glyph1 --max 2 MODELS/Example/asp/example.asp > MODELS/Example/stories/example4.stories

Get final sets of stories considering constraint (v):

        SCRIPTS/stories/stories --clabel --max 2 MODELS/Example/asp/example.asp > MODELS/Example/stories/example5.stories

sbgnpd2an/sbgnpd2an
----------------

Get AN model under the general semantics:

    SCRIPTS/sbgnpd2an/sbgnpd2an --initial-state glyph1,glyph3,glyph7,glyph2 MODELS/Example/maps/example.sbgn > MODELS/Example/analysis/an/nostories/nostories.an

Get AN model under the stories semantics:

    SCRIPTS/sbgnpd2an/sbgnpd2an --story a=glyph0,glyph4,glyph1 --story atp=glyph7,glyph8 --initial-state glyph1,glyph3,glyph7,glyph2 --names-are-ids MODELS/Example/maps/example.sbgn > MODELS/Example/analysis/an/stories/stories.an

pint-export
----------------

Get reduced model (stories semantics) for goal a=glyph4 (story a, state aP):

    pint-export -i MODELS/Example/analysis/an/stories/stories.an --reduce-for-goal a=glyph4 -o MODELS/Example/analysis/an/stories/reduced/stories_a=glyph4.reduced.an

Get PRISM model (stories semantics) from AN model:

    pint-export -i MODELS/Example/analysis/an/nostories/nostories.an -l prism -o MODELS/Example/analysis/prism/nostories/nostories.nm

pint-mole
----------------

Check reachability of state aP of story a:

    pint-mole -i MODELS/Example/analysis/an/stories/reduced/stories_a=glyph4.reduced.an a=glyph4 > MODELSExample/analysis/reach/stories/stories_a=glyph4.reach

pint-export
----------------

Get State Transition Graph of an AN model

    pint-sg --state-graph MODELS/Example/analysis/stg/stories/stories.dot -i MODELS/Example/analysis/an/stories/stories.an

## Main files in MODELS/:

    RB_E2F/: contains all files related to the RB/E2F map
        maps/rb_e2f.sbgn:              the RB/E2F map in SBGN-ML format               | generated by MODELS/RB_E2F/scripts/maps/make_sbgn_from_cd.sh
        asp/rb_e2f.asp:                RB/E2F's compound graph in ASP                 | generated by MODELS/RB_E2F/scripts/asp/make_asp.sh
        stories/rb_e2f.stories:        maximal valid set of stories of the RB/E2F map | generated by MODELS/RB_E2F/scripts/stories/make_stories.sh
        analysis/an/nostories/:        AN models under the general sem.
            nostories.an:              AN model under the general sem.                | generated by MODELS/RB_E2F/scripts/analysis/an/nostories/make_an.sh
            simultaneity/:             AN models built to check simultaneity          | generated by MODELS/RB_E2F/scripts/analysis/an/nostories/simultaneity/make_an.sh
            reduced/:                  reduced models
                normal/:               from nostories.an                              | generated by MODELS/RB_E2F/scripts/analysis/an/nostories/reduced/disable_e2f1/make_reduced.sh
                disable_e2f1/:         when E2F1 is disabled                          | generated by MODELS/RB_E2F/scripts/analysis/an/nostories/reduced/disable_e2f1/make_reduced.sh
                disable_prev_phase/:   when prev. phase is disabled                   | generated by MODELS/RB_E2F/scripts/analysis/an/nostories/reduced/disable_prev_phase/make_reduced.sh
                simultaneity/:         for simultaneity                               | generated by MODELS/RB_E2F/scripts/analysis/an/nostories/reduced/simultaneity/make_reduced.sh
        analysis/an/stories/:          AN models under the stories sem.
            ...
        analysis/an/nostoriestriggers: AN models with transc. effects under the general sem.
            ...
        analysis/an/storiestriggers*:  AN models with transc. effects under the stories sem.
            ...
        analysis/phases/rb_e2f.phases: phases of the cell cycle

    ERK/:    contains all files related to the ERK map
        maps/erk.sbgn:              the ERK map in SBGN-ML format
        asp/erk.asp:                ERK's compound graph in ASP                 | generated by MODELS/ERK/scripts/asp/make_asp.sh
        stories/erk.stories:        maximal valid set of stories of the ERK map | generated by MODELS/ERK/scripts/stories/make_stories.sh

    PolyQ/:  contains all files related to the PolyQ map
        maps/polyq.sbgn:                                the PolyQ map in SBGN-ML format
        asp/polyq.asp:                                  PolyQ's compound graph in ASP                     | generated by MODELS/PolyQ/scripts/asp/make_asp.sh
        stories/polyq.stories:                          maximal valid set of stories of the PolyQ map     | generated by MODELS/PolyQ/scripts/stories/make_stories.sh
        analysis/an/stories/stories.an:                 AN model under the stories sem.                   | generated by MODELS/PolyQ/scripts/analysis/an/stories/make_an.sh
        analysis/prism/stories/noprobas/noprobas.prism: PRISM model under the stories sem. with no probas | generated by MODELS/PolyQ/scripts/analysis/prism/stories/noprobas/make_prism.sh
        analysis/prism/stories/probas/probas.prism:     PRISM model under the stories sem. with ptobas
        analysis/prism/stories/probas/property.csl:     the probavility to be computed on the prism model
        analysis/results/probas.txt:                    probas computed from the two previous files       | generated by MODELS/PolyQ/scripts/analysis/results/get_probas.sh
        analysis/results/probas.png:                    results plotted                                   | generated by MODELS/PolyQ/scripts/analysis/results/make_gnuplot_graph.sh

    Example/:  contains all files related to the example map
        ...
