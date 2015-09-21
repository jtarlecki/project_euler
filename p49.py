counts = [1,2]
primes = [2]
i = primes[-1] + 1
digits = 4

def is_prime(n):
    for prime in primes:
        if prime > n**(0.5):
            return True
        if n % prime == 0:
            return False

def is_permutations(a_list):
    for a in a_list:
        if not permutable(list(str(a_list[0])), str(a)):
            return False
    return True
        

def permutable(checklist, num):
    for digit in num:
        try:
            checklist.pop(checklist.index(digit))
        except:
            return False
    return True


for count in counts:
    still_looking = True
    while still_looking:
        if is_prime(i):
            primes.append(i)                 
            if len(str(i)) == digits:
                for prime in primes:
                    half = (i + prime)/2
                    if len(str(prime)) == digits and len(str(half)) == digits:
                        if half in primes and half != i:
                            if is_permutations([prime, half, i]):
                                print '\n', count, [prime, half, i]
                                print 'ans[%d] = %d%d%d' % (count, prime, half, i)
                                still_looking = False
        i+=1
