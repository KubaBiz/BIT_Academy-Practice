from solution import prime
import pytest

@pytest.mark.parametrize("test_input, expected", [(1, False), (2, True), (-1, False), (0, False)] )

def test_1(test_input, expected):
    assert prime(test_input) == expected
a = True

def test_2():
    A = [7043, 6827, 7351, 2711]
    for x in A:
        if prime(x) != True:
            a = False
        assert prime(x)==True

@pytest.mark.skipif(a == False, reason="Nie zdało testu 2")
class TestBig:
    def test_1(self):
        assert prime(805469181901) == True
    def test_2(self):
        assert prime(997*997) == False
    def test_3(self):
        assert prime(26525285981219105863630847) == False