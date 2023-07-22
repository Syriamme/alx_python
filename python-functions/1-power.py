"""
Given two numbers (a, b), calculate the power and return a value
:param a: int
:param b: int
:return: int
example
>>> power(2, 3
8
return (a ** b)
"""
def power(a, b):
    result = 1
    if b >= 0:
        for i in range(b):
            result *= a
    else:
        b = -b
        for i in range(b):
            result *= a
        result = 1 / result
    return result
