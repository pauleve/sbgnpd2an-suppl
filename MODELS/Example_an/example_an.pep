PEP
PTNet
FORMAT_N
PL
1"a=0"M1
2"a=1"M0
3"a=2"M0
4"b=0"M1
5"b=1"M0
6"c=0"M1
7"c=1"M0
TR
1"c 0 -> 1 when a=1"
2"a 1 -> 2 when c=1"
3"a 0 -> 1 when b=1"
4"b 1 -> 0 when a=0 and c=0"
TP
1<2
1<7
2<3
2<7
3<2
3<5
4<1
4<4
4<6
PT
1>3
1>4
2>1
2>2
5>3
5>4
6>1
6>4
7>2
