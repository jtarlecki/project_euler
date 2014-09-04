#nth = 6
nth = 10001
primes = [2]

i = primes[0]

def prime_check(number):
    for prime in primes:
        if number % prime == 0:
            return False
    #primes.append(number)
    return True

while len(primes) < nth:
    if prime_check(i):
        primes.append(i)
    i+=1

print primes[len(primes)-1]