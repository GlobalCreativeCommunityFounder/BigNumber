"""
This file contains code for the arbitrary precision number library "BigNumber".
Author: GlobalCreativeCommunityFounder
"""


# Importing necessary libraries
from mpmath import *
mp.pretty = True


# Creating BigNumber class


class BigNumber:
    """
    This class represents a BigNumber object.
    """

    def __init__(self, value):
        # type: (str or float or int or mpf) -> None
        self.value: mpf = value if isinstance(value, mpf) else mpf(value)

    def __add__(self, other):
        # type: (BigNumber or str or float or int or mpf) -> BigNumber
        if isinstance(other, BigNumber):
            return BigNumber(self.value + other.value)
        else:
            return BigNumber(self.value + other)

    def __sub__(self, other):
        # type: (BigNumber or str or float or int or mpf) -> BigNumber
        if isinstance(other, BigNumber):
            return BigNumber(self.value - other.value)
        else:
            return BigNumber(self.value - other)

    def __mul__(self, other):
        # type: (BigNumber or str or float or int or mpf) -> BigNumber
        if isinstance(other, BigNumber):
            return BigNumber(self.value * other.value)
        else:
            return BigNumber(self.value * other)

    def __truediv__(self, other):
        # type: (BigNumber or str or float or int or mpf) -> BigNumber
        if isinstance(other, BigNumber):
            return BigNumber(self.value / other.value)
        else:
            return BigNumber(self.value / other)

    def __mod__(self, other):
        # type: (BigNumber or str or float or int or mpf) -> BigNumber
        if isinstance(other, BigNumber):
            return BigNumber(self.value % other.value)
        else:
            return BigNumber(self.value % other)

    def __floordiv__(self, other):
        # type: (BigNumber or str or float or int or mpf) -> BigNumber
        if isinstance(other, BigNumber):
            return BigNumber(floor(self.value / other.value))
        else:
            return BigNumber(floor(self.value / other))

    def __pow__(self, other):
        # type: (BigNumber or str or float or int or mpf) -> BigNumber
        if isinstance(other, BigNumber):
            return BigNumber(floor(self.value ** other.value))
        else:
            return BigNumber(floor(self.value ** other))

    def __int__(self):
        # type: () -> int
        return int(self.value)

    def squared(self):
        # type: () -> BigNumber
        return self.__pow__(2)

    def cubed(self):
        # type: () -> BigNumber
        return self.__pow__(3)

    def __float__(self):
        # type: () -> float
        if self.value < mpf("2.2250738585072014e-308"):
            raise Exception("Underflow! The BigNumber object is too small to be converted to a float!")
        elif self.value > mpf("1.7976931348623157e+308"):
            raise Exception("Overflow! The BigNumber object is too large to be converted to a float!")
        else:
            return float(self.value)

    def __eq__(self, other):
        # type: (object) -> bool
        if isinstance(other, BigNumber):
            return self.value == other.value
        else:
            return False

    def __gt__(self, other):
        # type: (object) -> bool
        if isinstance(other, BigNumber):
            return self.value > other.value
        else:
            return False

    def __ge__(self, other):
        # type: (object) -> bool
        if isinstance(other, BigNumber):
            return self.value >= other.value
        else:
            return False

    def __lt__(self, other):
        # type: (object) -> bool
        if isinstance(other, BigNumber):
            return self.value < other.value
        else:
            return False

    def __le__(self, other):
        # type: (object) -> bool
        if isinstance(other, BigNumber):
            return self.value <= other.value
        else:
            return False

    def __ne__(self, other):
        # type: (object) -> bool
        if isinstance(other, BigNumber):
            return self.value != other.value
        else:
            return True

    def __pos__(self):
        # type: () -> BigNumber
        return BigNumber(self.value)

    def __neg__(self):
        # type: () -> BigNumber
        return BigNumber(self.value * -1)

    def __abs__(self):
        # type: () -> BigNumber
        if self.value < 0:
            return self.__neg__()
        return self.__pos__()

    def __floor__(self):
        # type: () -> BigNumber
        return BigNumber(floor(self.value))

    def __ceil__(self):
        # type: () -> BigNumber
        return BigNumber(ceil(self.value))

    def __and__(self, other):
        # type: (BigNumber or str or float or int or mpf) -> BigNumber
        if self.value == 0:
            return self
        else:
            if isinstance(other, BigNumber):
                return other
            else:
                return BigNumber(mpf(other))

    def __or__(self, other):
        # type: (BigNumber or str or float or int or mpf) -> BigNumber
        if self.value != 0:
            return self
        else:
            if isinstance(other, BigNumber):
                return other
            else:
                return BigNumber(mpf(other))

    def __str__(self):
        # type: () -> str
        return str(self.value)


# Creating additional methods for BigNumber class.


def to_mpf(big_num: BigNumber) -> mpf:
    return mpf(big_num.value)


def sqrt(big_num: BigNumber) -> BigNumber:
    return big_num.__pow__(0.5)


def cbrt(big_num: BigNumber) -> BigNumber:
    return big_num.__pow__(1 / 3)


def sin(big_num: BigNumber) -> BigNumber:
    return BigNumber(sin(big_num.value))


def cos(big_num: BigNumber) -> BigNumber:
    return BigNumber(cos(big_num.value))


def tan(big_num: BigNumber) -> BigNumber:
    return BigNumber(tan(big_num.value))


def cosec(big_num: BigNumber) -> BigNumber:
    return BigNumber("1") / BigNumber(sin(big_num.value))


def sec(big_num: BigNumber) -> BigNumber:
    return BigNumber("1") / BigNumber(cos(big_num.value))


def cot(big_num: BigNumber) -> BigNumber:
    return BigNumber("1") / BigNumber(tan(big_num.value))


def sinh(big_num: BigNumber) -> BigNumber:
    return BigNumber(sinh(big_num.value))


def cosh(big_num: BigNumber) -> BigNumber:
    return BigNumber(cosh(big_num.value))


def tanh(big_num: BigNumber) -> BigNumber:
    return BigNumber(tanh(big_num.value))


def cosech(big_num: BigNumber) -> BigNumber:
    return BigNumber("1") / BigNumber(sinh(big_num.value))


def sech(big_num: BigNumber) -> BigNumber:
    return BigNumber("1") / BigNumber(cosh(big_num.value))


def coth(big_num: BigNumber) -> BigNumber:
    return BigNumber("1") / BigNumber(tanh(big_num.value))


def factorial(big_num: BigNumber) -> BigNumber:
    return gamma(big_num.value + mpf("1"))


def ln(big_num: BigNumber) -> BigNumber:
    return log(big_num.value)


def log_e(big_num: BigNumber) -> BigNumber:
    return ln(big_num)


def log_10(big_num: BigNumber) -> BigNumber:
    return log10(big_num.value)


def log_base(big_num: BigNumber, base: BigNumber or mpf or float or int) -> BigNumber:
    if isinstance(base, BigNumber):
        return log_10(big_num) / log_10(base)
    else:
        return log_10(big_num) / log10(mpf(base))
