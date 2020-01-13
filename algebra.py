__version__ = '0.0.1'


def phi(n: int) -> int:
    """Euler function

    Parameters:
    n (int): Number

    Returns:
    int: Returning value
    """

    res, i = n, 2

    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i

            res -= res // i

        i += 1

    if n > 1:
        res -= res // n

    return res
