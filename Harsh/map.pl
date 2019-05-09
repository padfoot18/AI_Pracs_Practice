city(mumbai).
city(nagpur).
city(ahmedabad).
city(pune).

distance(mumbai,pune,300).
distance(pune,nagpur,400).
distance(mumbai,ahmedabad,1000).

indirect_distance(X,X,0).

indirect_distance(X,Y,Z):-
	distance(Y,X,Z).

indirect_distance(X,Y,Z):-
	distance(X,Y,Z).

indirect_distance(X,Y,Z):-
	distance(X,I,A) , distance(I,Y,B), Z is A+B.

interact:-
	writeln("Enter source"),
	read(Source),
	writeln("Enter destination"),
	read(Dest),
	indirect_distance(Source,Dest,Dist),
	writeln(Dist).
