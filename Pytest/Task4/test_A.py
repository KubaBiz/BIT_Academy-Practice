from function import square
from random import randint
import pytest
# Napisać 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie

class Test_1:
    def test_1(self):
        x = randint(-10,10)
        assert square(x) == x**2

    def test_2(self):
        assert square(0) == 0

    def test_3(self):
        assert square(1) == 1

    def test_4(self):
        assert square(-2) == 4

class Test_2:
    def test_1(self):
        x = randint(-1000, 1000)
        assert square(x) == x ** 2

    def test_2(self):
        x = randint(-1000, 1000)
        assert square(x) == x ** 2

    def test_3(self):
        x = randint(-1000, 1000)
        assert square(x) == x ** 2

    def test_4(self):
        x = randint(-1000, 1000)
        assert square(x) == x ** 2
a = True
class Test_3:
    def test_1(self):
        x = randint(10**4, 10**6)
        if square(x) != x ** 2:
            a = False
        assert square(x) == x ** 2

    def test_2(self):
        x = randint(10**4, 10**6)
        if square(x) != x ** 2:
            a = False
        assert square(x) == x ** 2

    def test_3(self):
        x = randint(10**4, 10**6)
        if square(x) != x ** 2:
            a = False
        assert square(x) == x ** 2

    def test_4(self):
        x = randint(10**4, 10**6)
        if square(x) != x ** 2:
            a = False
        assert square(x) == x ** 2
@pytest.mark.skipif(a == True, reason="Nie zdało testu 3")
class Test_4:
    def test_1(self):
        x = randint(10 ** 12, 10 ** 13)
        assert square(x) == x ** 2

    def test_2(self):
        x = randint(10 ** 12, 10 ** 13)
        assert square(x) == x ** 2

    def test_3(self):
        x = randint(10 ** 12, 10 ** 13)
        assert square(x) == x ** 2

    def test_4(self):
        x = randint(10 ** 12, 10 ** 13)
        assert square(x) == x ** 2
