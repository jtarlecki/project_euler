def triangle(n):
    return n*(n+1)/2

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)

tri_list =[]
pent_list = []
hex_list = []
n = 1 
still_looking = True
f = 0

while still_looking:
    n+=1
    t = triangle(n)
    tri_list.append(t)
    pent_list.append(pentagonal(n))
    hex_list.append(hexagonal(n))
    if t in pent_list and t in hex_list:
        f+=1
        t_i = n
        p_i = pent_list.index(t) + 2 # we started at python index(1) which is (2) by the formula count
        h_i = hex_list.index(t) + 2        
        print '\n', 'triangle set <%d>' % f
        print t_i, triangle(t_i)
        print p_i, pentagonal(p_i)
        print h_i, hexagonal(h_i)        
        still_looking = f < 2
