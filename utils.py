def fac(n):
    if n <= 1: return 1
    return n * f(n-1)

def fac_mod(x, p):
    if x <= 1: return 1
    return (x * fac_mod(x-1, p)) % p

def is_prime(p):
    # Wilson's theorem
    return (fac_mod(p-1, p) + 1) % p == 0

def is_five_power(n):
    while n >= 5:
        n //= 5
    return n == 1

def is_two_power(n):
    while n >= 2:
        n //= 2
    return n == 1
