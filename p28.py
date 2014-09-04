lim = 1001
diags = [1]
n = i = diags[0]

while n < lim**2:
	for x in range(4):
		n+=2*i
		diags.append(n)
	i+=1
	
print '\nSum of numbers on the diagonals in a %d x %d sprial = %d\n' % (lim, lim, sum(diags))
# 669171001
