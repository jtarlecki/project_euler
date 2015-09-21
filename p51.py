class Primes(object):
    
    def __init__(self):
        self.primes = [2]
        
    def is_prime(self, n):
        self.build_primes(n)
        return n in self.primes
            
    def build_primes(self, n):
        i = self.primes[-1] + 1
        while not i > n:
            if self.prime_check(i):
                self.primes.append(i)
            i+=1   
        pass
    
    def prime_check(self, n):
        for prime in self.primes:
            if prime > n**(0.5):
                return True
            if n % prime == 0:
                return False        
    
class Scoreboard(object):
    
    def __init__(self):
        self.prime = 2
        self.prime_count = 0
        self.prime_list = []
    
    def is_leader(self, primes):
        if len(primes) > self.prime_count:
            self.prime_count = len(primes)
            self.prime = min(primes)
            self.prime_list = primes
    
    def results(self):
        print 'prime:', self.prime
        print 'count: ', self.prime_count
        print 'primes: ', self.prime_list
    
class Number(object):
    
    def __init__(self, n, primes, score):
        if primes.is_prime(n):
            self.n = n
            self.p = primes
            self.score = score       
            self.n_str = str(n)
            self.n_list = list(str(n))
            self.get_binary_list()
            self.find_primes()
        
    def get_binary_list(self):

        length = len(self.n_str)
        b = ['1' for x in range(length)]
        binary = ''.join(b)
        number = int(binary, base=2)
        self.binaries = []
        self.b_loop = []
        for num in range(number):
            x = num + 1             # ignore n x 0
            b = bin(x)[2:]
            
            while len(b) < length:
                b = '0' + b
            #print x,b
            
            self.binaries.append(b)
            a = []
            for letter in b:
                a.append('1'==letter)
            self.b_loop.append(a)
        
        #print self.n, self.binaries
        
    def find_primes(self):
        #print '******************************************'
        #print 'n = ' ,self.n
        #print '******************************************', '\n'
        for boolean in self.b_loop:
            prime_list = []
            for i in range(10):
                num = ''
                index = 0
                for b in boolean:
                    if b:
                        num += str(i)
                    else:
                        num += self.n_list[index]
                    index+=1
                if num[0] != '0': # rid self of leading zero number 03 != 3 by problem definition
                    num = int(num)
                    #print '','','num = ', num
                    if self.p.is_prime(num):
                        prime_list.append(num)
            self.score.is_leader(prime_list)
            #print '', '------------'
            #print '', 'primes = ', len(prime_list), '\n'
        pass
        

s = Scoreboard()
p = Primes()
i = 15          # 10**(digits-1)
threshold = 7

while s.prime_count < threshold:
    Number(i, p, s)
    i+=2

s.results()
