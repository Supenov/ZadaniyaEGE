import math

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(math.isqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def f(limit=1_125_001):
    results = []
    i = limit

    while len(results) < 5:
        prime_divs = []
        for j in range(2, math.isqrt(i) + 1):
            if i % j == 0:
                if is_prime(j):
                    prime_divs.append(j)
                if j != i // j and is_prime(i // j):
                    prime_divs.append(i // j)
        
        if prime_divs:
            prime_divs = sorted(set(prime_divs))
            for x in prime_divs:
                if str(x)[-1] == '7' and x != i and x != 7:
                    results.append((i, x))
                    print(i, x)
        i += 1

f()
