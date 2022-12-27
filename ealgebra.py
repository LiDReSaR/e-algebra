__version__ = '0.0.4'


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


def gcd(x: int, y: int) -> int:
    """Greatest Common Divisor

    Parameters:
    x (int): Number
    y (int): Number

    Returns:
    int: Result
    """

    while y > 0:
        x, y = y, x % y

    return x


def lcm(x: int, y: int) -> int:
    """Least Common Multiplier

    Parameters:
    x (int): Number
    y (int): Number

    Returns:
    int: Result
    """

    return x // gcd(x, y) * y
