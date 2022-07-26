from cmplex import C

# Napisać testy sprawdzające dodawanie liczb zespolonych
# w załączonym pliku

def test_1():
    assert C(1,2) + C(2,2) == C(3,4)

def test_2():
    assert C(0,0) + C(0,0) == C(0,0)

def test_3():
    assert C(-1000,1000) + C(500, -400) == C(-500, 600)

def test_4():
    assert C(1,1) + C(2,2) + C(3,3) == C(6,6)