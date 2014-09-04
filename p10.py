
#lim = 10
lim = 2*10**6
primes = [2]

i = primes[0]

def prime_check(number):
    for prime in primes:
        if number % prime == 0:
            return False
    return True


while i < lim:
    if prime_check(i):
        primes.append(i)
    i+=1
    if i % 100 == 0:
        print i
    
#print primes
print 'sum(primes) = ', sum(primes)