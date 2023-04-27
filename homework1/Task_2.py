"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from numpy import *
from collections import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    a, b = 0, 1
    for n in data:
        if n < a + b:
            if n != b:
                return False
            a, b = b, a + b
        else:
            return False
    return True

