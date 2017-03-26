import timeit

def primes(kmax):
    p = [None]*1000
    result = []
    if kmax > 1000:
        kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result

def time_cprimes(n=10):
    import primes
    return primes.cprimes(n)

def time_primes(n=10):
    return primes(n)

# https://docs.python.org/3.6/library/timeit.html?highlight=timeit#module-timeit
if __name__ == '__main__':
    elapsed = timeit.timeit('time_primes()', globals=globals())
    print("primes: {} seconds".format(elapsed))
    elapsed = timeit.timeit('time_cprimes()', globals = globals())
    print("cprimes: {} seconds".format(elapsed))

