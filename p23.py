def sum_divisors(n):
    
    i = 1
    divisors = []
    
    while not i > n/2:
        if n % i == 0:
            divisors.append(i)
        i+=1
    
    return sum(divisors)
  
def perfect_number(n):
    return sum_divisors(n) == n
 
def abundant_number(n):
    return sum_divisors(n) > n
 
def deficient_number(n):
    return sum_divisors(n) < n

lim = 28123
i = 1
abundant_numbers = []

while not i > lim:
    if abundant_number(i):
        abundant_numbers.append(i)
    i+=1

def sum_abundant(n, abundants):
    for abundant in abundants:
        if abundant > n:
            return False
        elif n - abundant in abundants:
            return True
    return False
    
not_in_abundants = []
lower_bound = 24
i = 1

while not i > lim:
    if i < lower_bound:
        not_in_abundants.append(i)
    elif not sum_abundant(i, abundant_numbers):
        not_in_abundants.append(i)
    i+=1

print sum(not_in_abundants)

# != 297604144