# Looping through primes would be better
# Certain primes create the longs chains
# Observed to be chain = P-1 for certain primes
# After observing, I reversed the order

start = 2
lim = 900           #1000
d = 999             #start
pattern_checks = 4  #10 is REALLY long

class Repeater(object):
    
    def __init__(self):
        self.has_pattern = False
    
    def found(self, decimal_place, repeat_pattern, decimal):
        non_pattern = ''
        self.decimal_place = decimal_place        
        self.repeat_pattern = repeat_pattern
        self.has_pattern = True
        self.pattern_length = len(self.repeat_pattern)
        if self.decimal_place > 0:
            non_pattern = decimal[0:decimal_place]
        self.decimal = '0.%s(%s)' % (non_pattern, self.repeat_pattern)
        
def pattern_search(decimal_list, pattern_accuracy):
    
    def find_pattern(test, items, e):
        
        chunks = len(items)/e
        
        for chunk in range(0,chunks):
            if items[chunk*e:chunk*e+e] != test:
                return False
        return True

    is_pattern = False
    repeater = Repeater()
    
    if not len(decimal_list) < pattern_accuracy:
        
        decimal = ''.join(decimal_list)
        evals = len(decimal_list)/pattern_accuracy
        e = 1
        
        while not (e > evals or is_pattern):
            i = 0
            iterations = len(decimal_list) % (e*pattern_accuracy)
            while not i > iterations:
                check = decimal[i:i+e]
                ddd = decimal[i:i+(pattern_accuracy*e)]
                is_pattern = find_pattern(check, ddd, e)
                if is_pattern:
                    repeater.found(i,check, decimal)
                i+=1
            e+=1
        
    return repeater

ans = []
pattern_lengths = []

while d > lim: #< lim:
    r = 1
    n = 1
    decimals = []
    i = ''
    pattern = False
    
    while not pattern:
        r*=10
        # i += str(r/d)
        decimals.append(str(r/d))
        r = r % d
        n+=1
        if r != 0:
            rep = pattern_search(decimals, pattern_checks)
            pattern = rep.has_pattern
            if pattern:
                # answer = [d, rep.decimal]
                pattern_lengths.append(rep.pattern_length)
        else:
            pattern = True
            # answer = [d, '0.%s' % i]
            pattern_lengths.append(0)
    
    # print answer

    d-=1 #+=1
    
max_pattern_length = max(pattern_lengths)
print 'final', pattern_lengths.index(max_pattern_length) + start
