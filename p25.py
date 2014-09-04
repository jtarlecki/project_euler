fib = [1,1,2]	# initial seq
lim = 10**3	

while len(str(fib[-1])) < lim:
	fib.append(fib[-1] + fib[-2])

print 'First term to contain %d digits = %d' % (lim, len(fib))