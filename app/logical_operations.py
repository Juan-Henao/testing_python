""" asd """


def is_even(n: int) -> bool:
    """ asd """

    return n % 2 == 0


def is_odd(n: int) -> bool:
    """ asd """

    return n % 2 != 0


def is_prime(n: int) -> bool:
    """ asd """

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """ asd """

    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """ asd """

    return abs(a * b) // gcd(a, b)
