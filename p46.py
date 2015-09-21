primes = [2]
i = primes[-1]+1  	# skip "2" for convenience (added above)
odd_composites = []
c = True

def is_prime(n):
    for prime in primes:
        if prime > n**(0.5):
            return True
        if n % prime == 0:
            return False

def conjecture(n):
    for prime in primes:
        a = 1
        while not prime + 2*a**2 > n:
            if prime + 2*a**2 == n:
                return True
            a+=1
    return False

while c:
    if is_prime(i):
        primes.append(i)
    else:
        odd_composites.append(i)
        c = conjecture(i)
    i+=2
    
print 'max(odd_composites): ', max(odd_composites)
    
    
    
	
    
    
    