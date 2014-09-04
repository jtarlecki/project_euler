i = 2
exp = 5
digit_powers = []

while i < 10**(exp+1): 
	digits = list(str(i))
	sum_powers = 0
	for digit in digits:
		sum_powers += int(digit)**exp
	if sum_powers == i:
		digit_powers.append(i)
	i+=1

print digit_powers
print 'Sum of digit powers', sum(digit_powers)
