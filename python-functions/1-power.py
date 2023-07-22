def pow(x, y):
    """
    Given two numbers, (x, y), return the power.
    :param x: int
    :param y: int
    :return: int
    """
    power = 1
    for _ in range(y):
        power *= x
    return power

# Test cases
assert pow(2, 3) == 8
assert pow(5, 0) == 1
assert pow(13, 15) == 68719476736
assert pow(5, 8) == 390625