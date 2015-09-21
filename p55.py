palindrome_limit = 50

def rev(n):
    n = list(str(n))
    n.reverse()
    return int(''.join(n))
    
def add_with_rev(n):
    return n + rev(n)

def is_palendrome(n):
    return n == rev(n)


n = 1
#n = 10677   
limit = 10**4
Lychrel_number_count = 0


while n < limit:    
    i = 1   
    x = add_with_rev(n) 
    while not is_palendrome(x) and i < palindrome_limit:
        x = add_with_rev(x)
        i+=1
    if i == palindrome_limit:
        Lychrel_number_count+=1
    n+=1
    
print 'Lychrel_number_count = ', Lychrel_number_count 