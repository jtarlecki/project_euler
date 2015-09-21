def is_pandigital(num, lim):
    num = list(str(num))
    y = [str(i) for i in range(1, lim)]
    for x in y:
        try:
            num.pop(num.index(x))
        except:
            return False
    return num == []

def is_prime(n):
    for prime in primes:
	if prime > n**(0.5):
	    return True
	if n % prime == 0:
	    return False

primes = [2]
lim = 9
i = primes[-1]+1

while not len(str(i)) > lim:
    if is_prime(i):
	primes.append(i)
	if is_pandigital(i, len(str(i))+1):
	    pandigital_max = i
    i+=1

print pandigital_max