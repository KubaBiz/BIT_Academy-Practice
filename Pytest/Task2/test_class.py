from function import is_prime
from random import randint

class TestMini:
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>

    def test_1(self):
        assert is_prime(-1) == False
    def test_2(self):
        assert is_prime(0) == False
    def test_3(self):
        assert is_prime(1) == False
    def test_4(self):
        assert is_prime(2) == True
    def test_5(self):
        assert is_prime(3) == True
    def test_6(self):
        assert is_prime(4) == False
    def test_7(self):
        assert is_prime(5) == True
    def test_8(self):
        assert is_prime(6) == False

class TestMid:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>

    def test_1(self):
        assert is_prime(13649) == True

    def test_2(self):
        assert is_prime(99733) == True

    def test_3(self):
        assert is_prime(113*113) == False

    def test_4(self):
        assert is_prime(56263) == True

    def test_5(self):
        assert is_prime(997*997) == False

class TestMaxi:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji

    def test_1(self):
        assert is_prime(10**12) == False

    def test_2(self):
        assert is_prime(999983*999983) == False

    def test_3(self):
        assert is_prime(1223487231231) == False

    def test_4(self):
        assert is_prime(10**13-12314251895) == False

    def test_5(self):
        assert is_prime(997*997) == False

