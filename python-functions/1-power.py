def power(a, b):
    """
    Given two numbers, (a, b), return the power.
    :a: int
    :b: int
    :return: int
    """
    power = 1
    for _ in range(b):
        power *= a
        return power