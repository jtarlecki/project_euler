lim = 100
seq = [] # don't worry about order, it's just a count

a = 2
while not a > lim:
	b = 2
	while not b > lim:
		if not a**b in seq:
			seq.append(a**b)
		b+=1
	a+=1

print 'distinct terms', len(seq)