#!/bin/bash
SCRIPTS/stories/stories --max 1 MODELS/Example/asp/example.asp > MODELS/Example/stories/example1.stories
SCRIPTS/stories/stories --max 2 MODELS/Example/asp/example.asp > MODELS/Example/stories/example2.stories
SCRIPTS/stories/stories --max 3 MODELS/Example/asp/example.asp > MODELS/Example/stories/example3.stories
SCRIPTS/stories/stories --story glyph3,glyph0 --story glyph8,glyph1 --max 2 MODELS/Example/asp/example.asp > MODELS/Example/stories/example4.stories
SCRIPTS/stories/stories --clabel --max 2 MODELS/Example/asp/example.asp > MODELS/Example/stories/example5.stories
