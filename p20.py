def factorial(n):
    ans = 1
    while n > 0:
        ans *= n
        n-=1    
    return ans

num = 100
sum_digits = 0

f = factorial(num)

for s in str(f):
    sum_digits += int(s)

print 'sum of the digits in the number %d = ' % num, sum_digits