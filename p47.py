counts = [2,3,4]
primes = [2]
i = primes[-1]+1  	# skip "2" for convenience (added above)
c_nums = {}


def is_prime(n):
    for prime in primes:
        if prime > n**(0.5):
            return True
        if n % prime == 0:
            return False

def get_prime_factors(n):
    factors = []
    for prime in primes:
        if n % prime == 0:
            factors.append(prime)
            while n % prime == 0:
                if n == prime:
                    return factors
                n/=prime

for count in counts:
    c_nums[count] = []
    while len(c_nums[count]) < count:
        if is_prime(i):
            primes.append(i)
        else:
            if len(get_prime_factors(i)) == count:
                if not i-1 in c_nums[count]:
                    c_nums[count] = []
                c_nums[count].append(i)                    
        i+=1
    print count, c_nums[count]
    
print '\n', 'consecutives_numbers: ', c_nums
print 'answer = ', c_nums[4][0]