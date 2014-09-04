primes = [2]

def quadratic(a, b, n):
	return n**2 + a*n + b

def build_primes(number):
	k = max(primes) 
	while number > max(primes):
		if is_prime(k):
			primes.append(k)
		k+=1
	
def is_prime(number):
	for prime in primes:
		if number % prime == 0:
			return False
	return True

n_max = 0
a_max = 0
b_max = 0
prod = 0

a = 0
b = 0
lim = 10**3

build_primes(lim)
primes.remove(primes[-1]) 	# function goes over limit, remove the last one
lim_primes = list(primes)	# create a list of primes to iterate through, for "a" and "b"

for a in lim_primes:
	for i in [-1,-1]: 
		a*=i
		#while b < lim:
		for b in lim_primes:
			for j in [-1,-1]:
				b*=j
				n = 0
				still_prime = True
				while still_prime:
					number = quadratic(a, b, n)
					build_primes(number)
					still_prime = number in primes
					n+=1
				print '--- a = ', a, 'b = ', b, 'n = ', n, '---'
				if n > n_max:
					n_max = n
					a_max = a
					b_max = b
					prod = a*b
					print '*******************'
					print 'new max = ', n_max
					print '*******************'
			#b+=1
	#a+=1

print 'a', a_max
print 'b', b_max
print 'n', n_max
print 'prod', prod
