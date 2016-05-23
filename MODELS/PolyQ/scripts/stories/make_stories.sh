#!/bin/bash
SCRIPTS/stories/stories \
 --initial-state glyph4,glyph41,glyph18 \
 --clabel \
 --max 2 \
 MODELS/PolyQ/asp/polyq.asp > MODELS/PolyQ/stories/polyq.stories
