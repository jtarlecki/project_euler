ans = 1000
limit = ans
i = limit


def check_pythag(c):
   if c - int(c) == 0:
      return True
   else:
      return False

a = 1

while a < limit:
   b = a + 1
   while b < limit:
      c_squared = a**2 + b**2
      c = c_squared**(.5)
      if check_pythag(c):
         c = int(c)
         if a + b + c == ans:
            print 'abc = ', a*b*c
      b+=1
   a+=1