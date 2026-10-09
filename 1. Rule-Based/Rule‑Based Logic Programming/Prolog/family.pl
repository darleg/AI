% Facts: Basic relationships
parent(john, mary).
parent(john, michael).
parent(susan, mary).
parent(susan, michael).
parent(mary, linda).
parent(mary, james).

male(john).
male(michael).
male(james).

female(susan).
female(mary).
female(linda).

% Rule: X is a father of Y if X is male and X is a parent of Y
father(X, Y) :-
    male(X),
    parent(X, Y).

% Rule: X is a mother of Y if X is female and X is a parent of Y
mother(X, Y) :-
    female(X),
    parent(X, Y).

% Rule: X is a grandparent of Y if X is a parent of Z and Z is a parent of Y
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Rule: X is a sibling of Y if they share a parent and are not the same person
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

% Rule: X is a sister of Y if X is female and sibling of Y
sister(X, Y) :-
    female(X),
    sibling(X, Y).

% Rule: X is a brother of Y if X is male and sibling of Y
brother(X, Y) :-
    male(X),
    sibling(X, Y).
