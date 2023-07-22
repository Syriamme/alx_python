def power(a, b):
    """
    Given two numbers (a, b), calculate the power and return a value
    :param a: int
    :param b: int
    :return: int
    example

    >>> power(2, 3)
    8
    return (a ** b)
    """
    results = 1
    if b >= 0:
        for i in range(b):
            results *= a
    else:
        b = -b
        for i in range(b):
            results *= a
            results = 1 / results
    return results