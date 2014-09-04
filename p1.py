lim=1000
sum_mult=0
multiples = [3,5]

def modtest(number, mults):
	for mult in mults:
		mod = number % mult
		if mod == 0:
			return number
	return 0

for i in range(1, lim):
	sum_mult += modtest(i, multiples)
print sum_mult


		
	