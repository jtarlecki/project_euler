exp = 1000 #15
base = 2
total = 0

numbers = list(str(base**exp))

for number in numbers:
    total += int(number)
    
print 'total = ', total