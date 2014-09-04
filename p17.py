class NumberToString(object):

    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hundred = 'hundred'
    thousand = 'thousand'

    def __init__(self, number):
        self.lim = 1000
        self.number = number
        self.str_list = list(str(number))
        self.count = len(self.str_list)
        self.num_list = []

        for s in self.str_list:
            self.num_list.append(int(s))
        
    def convert(self):
        if not self.number > self.lim:        
            if self.count == 1:
                return self.get_ones()
            if self.count == 2:
                return self.get_tens()
            if self.count == 3: 
                return self.get_hundreds()
            if self.count == 4:
                return 'onethousand'
        else:
            return "please input number less than %d" % self.lim
                
    def get_ones(self):
        return self.ones[self.number]
    
    def get_tens(self):
        
        t = self.num_list[-2] 
        o = self.num_list[-1]
        
        if t == 1:
            d = self.teens[o]
        else:
            d = self.tens[t] + self.ones[o]
        
        return d
        
    def get_hundreds(self):
        if self.get_tens() == '':
            return self.ones[self.num_list[-3]] + self.hundred 
        else:
            return self.ones[self.num_list[-3]] + self.hundred + 'and' + self.get_tens()
lim = 1000           
words = []

for i in range(1, lim+1):
    n = NumberToString(i)
    words.append(n.convert())
    
sum_letter_count = 0
c = 1
for word in words:
    print c, word
    sum_letter_count += len(word)
    c+=1
    
print 'sum_letter_count = ', sum_letter_count