n = 20
paths = []

for x in range(0,n+1):
    row = []
    for y in range(0,n+1):
        if 0 in [x,y]:
            row.append(int(not(x==0 and y==0)))
        else:
            row.append(paths[-1][y] + row[-1])      # above and to the left
            
    paths.append(row)

print 'Unique paths for %d x %d lattice:' % (n,n) , paths[-1][-1]