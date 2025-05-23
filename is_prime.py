import warnings
import math


def is_prime(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer")

    if n > 1_000_000:
        warnings.warn(
            f"Checking a large number ({n}) for primality may take significant time",
            RuntimeWarning
        )

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
