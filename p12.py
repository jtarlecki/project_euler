# highly divisible triangular number

#triangle_numbers = []
#triangle_factors = []

count_limit = 500

i = 1
tri = 0
f = 0

while not f > count_limit:
    tri+=i
    f = 0
    sq = int(tri**(0.5))
    # print tri, sq
    while sq > 0:
        if tri % sq == 0:
            f+=2
        sq-=1
    print f
    i+=1

# print triangle_numbers
# print triangle_factors

print 'ans = ', tri
