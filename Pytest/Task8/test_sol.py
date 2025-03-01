from solution import Next_prime
import pytest

class Test_small:
    def test_A(self):
        assert Next_prime(-1) == 2
        assert Next_prime(0) == 2
        assert Next_prime(1) == 2
        assert Next_prime(2) == 3
        assert Next_prime(3) == 5
        assert Next_prime(7) == 11
    def test_B(self):
        A = [2,	3, 5, 7, 11, 13, 17, 19, 23, 29,
            31,	37,	41,	43,	47,	53,	59,	61,	67,	71,
            73,	79,	83,	89,	97, 101]
        prime = 0
        for i in range(100):
            if i == A[prime]:
                prime += 1
            assert Next_prime(i) == A[prime]

class Test_big:
    def test_A(self):
        A = [10000019,	10000079,	10000103,	10000121,	10000139,	10000141,	10000169,	10000189,	10000223,	10000229,
10000247,	10000253,	10000261,	10000271,	10000303,	10000339,	10000349,	10000357,	10000363,	10000379,
10000439,	10000451,	10000453,	10000457,	10000481,	10000511,	10000537,	10000583,	10000591,	10000609,
10000643,	10000651,	10000657,	10000667,	10000687,	10000691,	10000721,	10000723,	10000733,	10000741,
10000747,	10000759,	10000763,	10000769,	10000789,	10000799,	10000813,	10000819,	10000831,	10000849]
        prime = 0
        for i in range(10000000, 10000848):
            if i == A[prime]:
                prime += 1
            assert Next_prime(i) == A[prime]