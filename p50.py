def is_prime(n):
    for prime in primes:
        if prime > n**(0.5):
            return True
        if n % prime == 0:
            return False

def consecutive_prime_count(n, prime_index):
    consec_primes = []
    while not prime_index > len(primes):
        # print 'n, prime_index', n, prime_index
        consec_primes.append(primes[prime_index])
        if sum(consec_primes) == n:
            return len(consec_primes)
        elif sum(consec_primes) > n:
            return 0
        prime_index+=1



lims = [10**2, 10**3, 10**6]
primes = [2]
i = primes[-1]+1
max_consec_prime_count = 0 
max_consec_prime = 0
 
for lim in lims:  
    while i < lim:
        if is_prime(i):
            primes.append(i)
            k = 0
            if i == 41:
                pass
            while len(primes) - k > max_consec_prime_count:
                c = consecutive_prime_count(i, k)
                if c > max_consec_prime_count:
                    max_consec_prime_count = c
                    max_consec_prime = i
                    # print i, max_consec_prime_count
                k+=1
        i+=2
    print lim, max_consec_prime, max_consec_prime_count