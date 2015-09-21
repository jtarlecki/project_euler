fname = 'p042_words.txt'

def tri_num(n):
	return (n*(n + 1))/2
	
n = 1
tri_nums = [1]
triangle_words = 0

f = open(fname, 'r')
words = f.read().replace('"','').split(',')
# print words

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_value = {}

# build dictionary of alphabet values
x = 1
for letter in alphabet:
    alphabet_value[letter] = x
    x+=1
	
for word in words:
	num = 0
	for letter in word:
		num += alphabet_value[letter]
	while num > max(tri_nums):
		n+=1
		tri_nums.append(tri_num(n))
		
	if num in tri_nums:
		triangle_words += 1

print 'triangle_words: ', triangle_words
