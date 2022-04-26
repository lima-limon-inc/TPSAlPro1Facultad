from random import choice

L = ["a", "b", "c", "d", "e", "f", "g"]

choices = choice(L)
while choices != "d":
    choices = choice(L)
    print(choices)
