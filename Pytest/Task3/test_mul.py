from cmplex import C
from random import randint

# Napisać testy sprawdzające mnożenie liczb zespolonych
# w załączonym pliku

def test_1():
    assert C(1,2) * C(2,2) == C(-2,6)

def test_2():
    assert C(0,0) * C(0,0) == C(0,0)

def test_3():
    x = C(randint(-1000,1000),randint(-1000,1000))
    y = C(randint(-1000,1000),randint(-1000,1000))
    assert x * y == C(x.x*y.x - x.y*y.y, x.x*y.y+y.x*x.y)

def test_4():
    assert C(1,1) * C(2,2) * C(4,3) == C(-12,16)