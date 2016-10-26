
# enumerate all prime numbers up to n
# brute force is to test each value and see if its divisible by sqrt(i)
# better approach, start with a bool array of prime candidates
# if we see a prime, sieve it, cross out all it's multiples

def enumeratePrimes(n):

    numbers = [True for i in range(n+1)]
    # set 0 and 1 to False
    numbers[0] = numbers[1] = False
    primes = []

    # iterate through a range, not the actual list
    for i in range(2, n+1):
        # sieve value if True
        if numbers[i] == True:
            primes.append(i)
            # start at i+i and step by i amount
            for j in range(i+i, n+1, i):
                numbers[j] = False

    return primes


n = 10
print 'the primes up to {} are {}'.format(n, enumeratePrimes(n))

n = 20
print 'the primes up to {} are {}'.format(n, enumeratePrimes(n))



