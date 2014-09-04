digits = 3
#print len(str(100))==digits

limit = 10**digits - 1
print 'start', limit

palindromes = []

def rev(num):
    num_list = list(str(num))
    num_list.reverse()
    rev_str = ''.join(num_list)   
    return int(rev_str)

n = limit
while n > 0:
    k = limit
    while k > 0:
        prod = n*k
        if prod == rev(prod):
            palindromes.append(prod)
        k-=1
    n-=1
    
print 'max_palindrome = ', max(palindromes)