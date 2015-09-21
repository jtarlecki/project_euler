def is_pandigital(num):
    num = list(str(num))
    y = [str(i) for i in range(1,10)]
    for x in y:
        try:
            num.pop(num.index(x))
        except:
            return False
    return num == []
            
def get_product(n, multipliers):
    prod = [str(n*i) for i in ints]
    return int(''.join(prod))

ints = [1,2]
max_pandigital = 0
lim = 9

while not len(ints) > lim:
    # check that prod length == 9, if not skip
    # if len(prod) > 9, get out of loop, add an int, start at n=1
    n = 1
    prod = 0
    while not len(str(prod)) > lim:        
        prod = get_product(n, ints)
        if len(str(prod)) == lim:
            if is_pandigital(prod):
                if prod > max_pandigital:
                    max_pandigital = prod
        n+=1 
    ints.append(ints[-1] + 1)

print 'max_pandigital = ', max_pandigital
        