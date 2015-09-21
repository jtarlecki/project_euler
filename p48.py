lim = 1000
p = []
digits = 10

for n in range(1, lim+1):
    if str(n) > digits:
        p.append(int(str(n**n)[-digits:]))
    else:
        p.append(n**n)

print str(sum(p))[-digits:]