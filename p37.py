def rev(num):
    num_list = list(str(num))
    num_list.reverse()
    rev_str = ''.join(num_list)   
    return int(rev_str)

def left_to_right(num):
    num = str(num)
    ans = []
    j = 0
    for n in num:
        ans.append(int(num[j:len(num)]))
        j+=1
    return ans

def right_to_left(num):
    num = str(num)
    ans = []
    j = 0
    for n in num:
        ans.append(int(num[0:len(num)-j]))
        j+=1
    return ans

def is_prime(n):
    
    if n > primes[0]:
	for prime in primes:
	    if prime > n**(0.5):
		return True
	    if n % prime == 0:
		return False
    else:
	return False

lim = 11
primes = [2]
i = primes[-1] + 1
truncatable_primes = []
excluded = [2, 3, 5, 7]

def is_list_prime(a_list):
    for a in a_list:
	if not a in primes:
	    return False
    return True

while len(truncatable_primes) < lim:
    
    if is_prime(i):
	primes.append(i)
	if not i in excluded:
	    if is_list_prime(left_to_right(i)):
		if is_list_prime(right_to_left(i)):
		    truncatable_primes.append(i)
    i+=1

print truncatable_primes
print 'sum of truncatable_primes = ', sum(truncatable_primes)