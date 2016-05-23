PEP
PTNet
FORMAT_N
PL
1"a=null"M0
2"a=glyph0"M0
3"a=glyph4"M0
4"a=glyph1"M1
5"glyph2=0"M0
6"glyph2=1"M1
7"glyph10=0"M1
8"glyph10=1"M0
9"glyph9=0"M1
10"glyph9=1"M0
11"glyph3=0"M0
12"glyph3=1"M1
13"atp=null"M0
14"atp=glyph7"M1
15"atp=glyph8"M0
TR
1"glyph9 0 -> 1 when a=glyph1 and atp=glyph7 and glyph10=0 and glyph2=1"
2"a glyph1 -> glyph0 when glyph10=1"
3"glyph3 1 -> 0 when a=glyph0 and glyph10=1"
4"a glyph1 -> glyph4 when glyph9=1"
5"atp glyph7 -> glyph8 when glyph9=1"
6"glyph10 0 -> 1 when a=glyph1 and glyph3=1 and glyph9=0"
7"glyph9 1 -> 0 when a=glyph4 and atp=glyph8"
8"glyph10 1 -> 0 when a=glyph0"
TP
1<4
1<6
1<7
1<10
1<14
2<2
2<8
3<2
3<8
3<11
4<3
4<10
5<10
5<15
6<4
6<8
6<9
6<12
7<3
7<9
7<15
8<2
8<7
PT
2>3
2>8
3>7
4>1
4>2
4>4
4>6
6>1
7>1
7>6
8>2
8>3
8>8
9>1
9>6
10>4
10>5
10>7
12>3
12>6
14>1
14>5
15>7
