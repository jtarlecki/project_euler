fib = [1,2]
four_mil = 4*(10**6)
sum_fib = 0

while fib[len(fib) - 1] < four_mil:
	next_num = fib[len(fib) - 1] + fib[len(fib) - 2]
	fib.append(next_num)

for i in fib:
	if i % 2 == 0:
		sum_fib+=i

print sum_fib

#4613732