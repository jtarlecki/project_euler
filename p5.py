i=1
limit = 20
mult = 1
multiple_found = False

n = limit

def is_multiple(number, limit):
    k = limit-1
    while k > 0:
        if number % k == 0:
            k-=1
        else:
            return False
    return True

while not multiple_found:
    num = i*limit
    multiple_found = is_multiple(num, limit)
    #print num
    i+=1
    
            
print 'ans', num
