class Results(object):
    
    def __init__(self):
        self.triangles = {}
          
    def update(self, triangle):
        if self.triangles.has_key(triangle.p):
            if not self.is_dupe(triangle, self.triangles[triangle.p]):
                self.triangles[triangle.p].append(triangle)
        else:
            self.triangles[triangle.p] = [triangle]
            
    def is_dupe(self, incoming, existing):
        for t in existing:
            if (t.a == incoming.a and t.b == incoming.b and t.c == incoming.c):
                return True
        return False
    
class Triangle(object):
    
    def __init__(self, legs):
        legs.sort()
        self.a = int(legs[0])
        self.b = int(legs[1])
        self.c = int(legs[2])
        self.p = self.a + self.b + self.c
        
lim = 1000
max_solutions = 0
result = Results()
legs = [i for i in range(1,lim)]
squares = [leg**2 for leg in legs]

c = 3

for a in legs:
    if a == 4:
        pass
    for b in legs:
        c = (a**2 + b**2)**(0.5)
        p = a + b + c
        if c**2 in squares and p < lim:
            t = Triangle([a, b, c])
            result.update(t) 
  
for k,v in result.triangles.items():
    if len(v) > max_solutions:
        max_solutions = len(v)
        p = k
    
    

    
print 'max_solutions = ', max_solutions
print 'p =', p
