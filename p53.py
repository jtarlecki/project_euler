def factorial(n):
    ans = 1
    while n > 0:
        ans *= n
        n-=1
    return ans

def combinatronics(n):
    r = 1
    count = 0 
    while r < n:
        c = factorial(n)/(factorial(r) * factorial(n-r))
        if c > 10**6:
            count+=1
        r+=1
    return count

lim = 100
count = 0
i = 23

while not i > lim:
    count += combinatronics(i)
    i+=1

print count