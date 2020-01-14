__version__ = '0.0.2'


def phi(n: int) -> int:
    """Euler function

    Parameters:
    n (int): Number

    Returns:
    int: Result
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


def binexp(x: int, n: int) -> int:
    """Binary exponentiation

    Parameters:
    x (int): Base
    n (int): Exponent (power)

    Returns:
    int: Result
    """

    res = 1

    while n > 0:
        if n & 1 > 0:
            res *= x

        x *= x
        n >>= 1

    return res
