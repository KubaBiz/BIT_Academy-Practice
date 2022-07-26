from cmplex import C
from random import randint

# Napisać testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku

def test_1():
    for i in range(10):
        assert C(i,i) != C(i,10)

def test_2():
    x = randint(-100,100)
    y = randint(-100,100)
    assert C(x,y) == C(x,y)