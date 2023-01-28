#!/usr/bin/python3

# Recall that a prime number can only be divided without a remainder by itself
# and the number 1. For example, 4 can be divided by 2 without a remainder, so
# it is not a prime number, but 5 can be divided by only itself and 1 without a
# remainder. How can you confirm whether a number is prime or not?


def discern_prime_number(number):
    # 0 and 1 are defined as non-prime, so just return False in those cases
    if number == 0 or number == 1:
        return False
    # The largest number that *could* divide into `number` would be half of it,
    # so that's the end of the iteration.
    maxDivisor = number // 2
    # Test every number between 2 and `maxDivisor` inclusive to see if it
    # modulo's into `number` with no remainder. If so, return False.
    for divisor in range(2, maxDivisor+1):
        if number % divisor == 0:
            return False
    # If control flow made it this far, then no number between 2 and
    # `maxDivisor` divides into `number` with no remainder, so it's prime;
    # return True.
    return True


assert discern_prime_number(5) is True
assert discern_prime_number(23) is True
assert discern_prime_number(45) is False


