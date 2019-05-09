father(asharam, jitendra).
father(asharam, rakesh).
father(asharam, tallika).
father(asharam, pravina).
father(asharam, kala).
father(jitendra, hardik).
father(jitendra, harsh).
father(jitendra, dhruvi).
father(rakesh, mahek).
father(shailesh, arpit).
father(shailesh, sejal).
father(dilip, nimesh).
father(dilip, pinal).
father(dilipkumar, kunal).
father(dilipkumar, nidhi).

mother(sharda, jitendra).
mother(sharda, rakesh).
mother(sharda, tallika).
mother(sharda, pravina).
mother(sharda, kala).
mother(shilpa, hardik).
mother(shilpa, harsh).
mother(shilpa, dhruvi).
mother(prarthna, mahek).
mother(pravina, arpit).
mother(pravina, sejal).
mother(kala, nimesh).
mother(kala, pinal).
mother(tallika, kunal).
mother(tallika, nidhi).

sibling(X,Y) :- father(A,X) , father(A,Y) , mother(B,X) , mother(B,Y) , X\=Y.
grandfather(X,Y) :- (father(X,Z) , father(Z,Y)) ; (father(X,Z) , mother(Z,Y)) , X\=Y.
grandmother(X,Y) :- mother(X,Z) , (father(Z,Y) ; mother(Z,Y)) , X\=Y.
couple(X,Y) :- father(X,Z) , mother(Y,Z) , X\=Y.
cousin(X,Y) :- sibling(A,B) , ((father(A,X) , father(B,Y)) ; (mother(A,X) , mother(B,Y)) ; (father(A,X) , mother(B,Y)) ; (mother(A,X) , father(B,Y))).
%cousin(X,Y) :- grandfather(A,X) , grandfather(A,Y) , X\=Y.