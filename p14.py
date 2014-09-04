start = 1
i = 0
n = start
max_number = 10**6
longest_chain = 0
longest_chain_start_number = 0

while start < max_number:
    
    n = start
    i = 0
    while not n == 1:
    
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        i+=1
        #print n
    
    if i > longest_chain:
        longest_chain = i
        longest_chain_start_number = start
    start+=1    

print 'longest_chain = ', longest_chain 
print 'longest_chain_start_number = ', longest_chain_start_number