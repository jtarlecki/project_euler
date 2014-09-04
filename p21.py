def d(n):
    i = 1
    divisors = []
    while not i > n/2:
        if n % i == 0:
            divisors.append(i)
        i+=1
    return sum(divisors)

a = 1
lim = 10000
amicables = []

while a < lim:
    b = d(a)
    if b == d(a) and d(b) == a and a != b:
        amicables.append(a)
    a+=1

print 'sum of all amicable numbers under %d = %d' % (lim, sum(amicables))


