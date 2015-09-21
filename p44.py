def pentagonal_num(n):
	return n*(3*n - 1)/2
	
# print [pentagonal_num(i) for i in range(1,11)]

i = 1
pentagonals = []
pairs = []
while i < 10**6:
	this_p = pentagonal_num(i)
	pentagonals.append(this_p)
	if len(pentagonals) > 2:
		# print this_p
		for j in pentagonals:
			k = this_p - j
			# print '', k, k in pentagonals
			if k in pentagonals:
				if abs(k - j) in pentagonals:
					pairs.append([j, k, j+k, abs(j-k)])
					print pairs
	i+=1

print pairs