person(aditya, m, carpenter, unmarried).
person(kiran, m, mechanic, married).
person(milan, m, mafia, unmarried).
person(ankita, f, baseball_player, unmarried).
person(shifa, f, meachanic, unmarried).

motive(money).
motive(jealousy).

previous_affair(kiran, ankita).
previous_affair(aditya, shifa).

killed(ankita).
probable_murder_weapon(rod).
crime_scene_object(ring).

% knowledge

wears_a(X, ring):-
person(X, _, _,  married).

has_a(X, gun):-
person(X, _, mafia, _).
has_a(X, pipe):-
person(X, _, mechanic, _).
has_a(X, bat):-
person(X, _, baseball_player, _).
has_a(X, saw):-
person(X, _, carpenter, _).

are_similar(rod, bat).
are_similar(rod, pipe).


suspect(X):-
motive(money), person(X, _, mafia, _).

suspect(X):-
motive(jealousy), person(X, m, _, _), previous_affair(X, Y), killed(Y).

suspect(X):-
has_a(X, Z), are_similar(Y, Z), probable_murder_weapon(Y).

suspect(X):-
wears_a(X, Z), crime_scene_object(Z).


killer(X):-
(wears_a(X, Z), crime_scene_object(Z)) , (has_a(X, A), are_similar(Y, A), probable_murder_weapon(Y)).


