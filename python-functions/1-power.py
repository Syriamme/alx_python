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
def pow(a, b):
    final = 1

    if b >= 0:
        for i in range(b):
            final *= a

    else:
        b = -b
        for i in range(b):
            final *= a
        final = 1 / final
        
    return final