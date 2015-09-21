class Fraction(object):
    
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator

    def flip(self):
        f = [self.n, self.d]
        self.n = f[1]
        self.d = f[0]
        
    def add(self, x):
        # we only add whole numbers here
        a = x*self.d
        self.n += a
    
    def num_check(self):
        n_len = len(str(self.n))
        d_len = len(str(self.d))
        if n_len > d_len:
            return True

lim = 1000
n = 0
count = 0

for n in range(lim):
    i = n
    if i == 0:
        f = Fraction(3,2)
    else:    
        ans = 5.0/2
        f = Fraction(5,2)
        while i > 0:
            f.flip()
            if i == 1:
                f.add(1)
            else:
                f.add(2)
            i-=1
    
    print '(%d) :' % (n+1), '%d/%d' %(f.n, f.d)
    if f.num_check():
        count+=1
    
print 'count = ', count

'''
(0)
1 + 1/2 = 3/2 

(1)
1 + 1/(2 + 1/2) = 
----------------------

5/2, 
flip, 
+ 1

(2)
1 + 1/(2 + 1/(2 + 1/2)) = 
-------------------------
5/2,
flip,
+ 2
flip,
+ 1


(3)
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 
---------------------------------
5/2, 
flip,
+ 2
flip, 
+ 2, 
flip
+ 1
'''
    