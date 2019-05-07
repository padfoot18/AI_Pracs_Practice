%parent(name,name)
%father(name,name)
%mother(name,name)
%male(name)
%female(name)
%brother(name,name)
%sister(name,name)

male(harsh).
male(jitesh).
male(suresh).
male(amit).

female(sumitra).
female(heer).
female(radha).
female(dimple).
female(aarohi).


parent(harsh,jitesh).
parent(harsh,sumitra).
parent(heer,sumitra).
parent(heer,jitesh).
parent(jitesh,suresh).
parent(jitesh,radha).
parent(aarohi,amit).
parent(aarohi,dimple).


father(X,Y) :- male(Y),parent(X,Y).
mother(X,Y) :- female(Y),parent(X,Y).
son(X,Y) :- male(X),parent(X,Y).
daughter(X,Y) :- female(X),parent(X,Y).
brother(X,Y) :- male(X),parent(X,Z),parent(Y,Z).
sister(X,Y) :- female(X),parent(X,Z),parent(Y,Z).
sibling(X,Y) :- parent(X,Z),parent(Y,Z),\+X=Y, \+Y=X.
grandfather(X,Y) :- male(Y),parent(X,Z),parent(Z,Y).
grandmother(X,Y) :- female(Y),parent(X,Z),parent(Z,Y).
