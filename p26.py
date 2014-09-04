start = 2
lim = 1000
d = start

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
            
            #print 'compare', items[chunk*e:chunk*e+e], test
            if items[chunk*e:chunk*e+e] != test:
                return False
        '''
        for item in items:
            if item != test:
                return False
        '''
        return True

    is_pattern = False
    repeater = Repeater()
    
    
    if not len(decimal_list) < pattern_accuracy:
        decimal = ''.join(decimal_list)
        evals = len(decimal_list)/pattern_accuracy
        '''
        print 'decimal', decimal
        print 'len(decimal_list)', len(decimal_list)
        print 'evals', evals
        '''
        if len(decimal_list) >= 60:
            pass
        e = 1
        
        while not (e > evals or is_pattern):
            i = 0
            iterations = len(decimal_list) % (e*pattern_accuracy)
            '''
            print e
            print pattern_accuracy
            print 'iters', iterations
            '''
            while not i > iterations:
                check = decimal[i:i+e]
                ddd = decimal[i:i+(pattern_accuracy*e)]
                '''
                print 'check', check
                print 'decimal[i:i+(pattern_accuracy*e)]', ddd
                '''
                if e==6:
                    pass                
                is_pattern = find_pattern(check, ddd, e)
                
                if is_pattern:
                    repeater.found(i,check, decimal)
                i+=1
            e+=1
        
    return repeater

ans = []
pattern_lengths = []

while d < lim:
    r = 1
    n = 1
    dec = []
    patterns = []
    decimals = []
    i = ''
    p = ''
    pattern = False
    while not pattern:
        r*=10
        i += str(r/d)
        decimals.append(str(r/d))
        dec.append(i)
        r = r % d
        p+=str(r)
        patterns.append(p) 
        n+=1
        '''
        print d, p, i
        print '\n>>>>>>>>>>  1/%d  <<<<<<<<<<<\n' % d        
        '''
        if r != 0:
            rep = pattern_search(decimals, 10)
            pattern = rep.has_pattern
            if pattern:
                answer = [d, rep.decimal]
                pattern_lengths.append(rep.pattern_length)
        else:
            pattern = True
            answer = [d, '0.%s' % i]
            pattern_lengths.append(0)
        '''
        print 'pattern', pattern
        print 'r', r
        '''
    ans.append(answer)
    print answer

    d+=1
    
max_pattern_length = max(pattern_lengths)
print 'final', pattern_lengths.index(max_pattern_length) + start

#print [str(i) for i in dec]