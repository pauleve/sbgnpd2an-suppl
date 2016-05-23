inStory(X):-gather(X,Y).
inStory(Y):-gather(X,Y).
#maximize {1,inStory,X:inStory(X),epn(X)}.
