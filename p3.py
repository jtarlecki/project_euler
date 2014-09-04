num = 600851475143
# num = 13195
factors = []
primes = []
devisors = [1]

def walk_thru_factors(number):
	i=2
	factors = []
	new_number = number
	while not i > new_number:
		if new_number % i == 0:
			factors.append(i)
			new_number = new_number / i
			print i
		else:
			i+=1
	print factors

walk_thru_factors(num)
	
	
	