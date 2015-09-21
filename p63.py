lim = 100  #random upper limit, i know this could be done much better
count = 0

def get_digit_count(num):
    return len(str(num))

i = 1
while not i > lim:
    j = 1
    while not j > lim:
        if j == get_digit_count(i**j):
            count+=1
        j+=1
    i+=1

print count