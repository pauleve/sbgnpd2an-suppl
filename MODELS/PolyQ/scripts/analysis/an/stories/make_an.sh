#!/bin/bash
SCRIPTS/sbgnpd2an/sbgnpd2an \
    --story glyph2,glyph41,glyph3,glyph38,glyph39 \
	--story glyph4,glyph5,glyph35 \
    --initial-state glyph14,glyph15,glyph17,glyph24,glyph4,glyph18,glyph41,glyph6 \
 MODELS/PolyQ/maps/polyq.sbgn > MODELS/PolyQ/analysis/an/stories/stories.an
