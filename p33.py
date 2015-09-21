numbers = []
fractions = []

for i in range(10,100):
	numbers.append(i)

def check_cancellations(n, d, i):
	b = 0==i
	num = list(str(n))
	denom = list(str(d))
	if float(denom[b]) != 0:
		if num[b] == denom[not b]:
			if float(num[not b]) / float(denom[b]) == float(n) / float(d):
				fractions.append([n,d])

for d in numbers:
	for n in numbers:
		if n < d:
			for x in [0,1]:
				check_cancellations(n, d, x)

print fractions

n = d = 1
for f in fractions:
	n*=f[0]
	d*=f[1]

print 'product:', '%d / %d' % (n,d)

i=2
lim = n**(.5)
while not i > lim:
	while n % i == 0 and d % i == 0:
		n/=i
		d/=i
	i+=1

print 'reduced product:', '%d / %d' % (n,d)
print 'denominator:', d