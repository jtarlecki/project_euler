def circular_number_list(n):
	circulars = []
	strings = list(str(n))
	x = len(strings)
	
	for i in range(x):
		s = ''
		for j in range(x):
			s+=strings[i]
			i+=1
			if i >= x:
				i=0
		circulars.append(int(s))
	
	return circulars 
	
def is_prime(n):
	for prime in primes:
		if prime > n**(0.5):
			return True
		if n % prime == 0:
			return False


primes = [2]
cicular_primes = []
lim = 10**6
i = primes[-1]+1

while i < lim:
	if is_prime(i):
		primes.append(i)
	i+=1
	
for prime in primes:
	circs = circular_number_list(prime)
	j = 0
	for c in circs:
		if c in primes:
			j+=1
	if j==len(circs):
		cicular_primes.append(prime)
	
	
print len(cicular_primes)
	




