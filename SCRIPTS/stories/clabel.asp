#show cand/2.

1 {cand(L,X):belong(L,X)} 1:-hasLabel(X);epn(X).
same(X,Y):-cand(L,Y);cand(L,X);epn(X);epn(Y);X!=Y.
:-not same(X,Y);gather(X,Y);epn(X);epn(Y);X!=Y.
