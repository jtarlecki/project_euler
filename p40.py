lim = 10**6
i = 1
decimal = ''

while not len(decimal) > lim:
    decimal += str(i)
    i+=1

d = 0
digits = []
n = prod = 1

while not d > lim:
    prod*=int(decimal[d])
    digits.append(int(decimal[d]))
    n+=1
    d = 10**n - 1
    
print digits
print prod
