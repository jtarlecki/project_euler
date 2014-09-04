# uses a file called p022_names.txt
fname = 'p022_names.txt'
check = 938

f = open(fname, 'r')
names = f.read().replace('"','').split(',')

names.sort()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_value = {}

# build dictionary of alphabet values
x = 1
for letter in alphabet:
    alphabet_value[letter] = x
    x+=1

x = 1
ans = 0
for name in names:
    letters = []
    for letter in name:
        letters.append(alphabet_value[letter])
    ans += x*sum(letters)    
    #if x == check:
        #print x, sum(letters), x*sum(letters)
    x+=1

print 'sum of names scores = %d' % ans

f.close()

