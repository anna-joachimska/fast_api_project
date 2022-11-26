
from sympy.ntheory.primetest import mr


def is_prime(number: int):
    max = 9223372036854775807
    if 1 < number < max:
        assert (number < max)
        ps = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        for i in range(1, 9):
            i = i + 1
            if mr(number, ps) == False:
                return False
            else:
                return True
    else:
        return False
