lim = 100
digit_sum = []

def get_digit_sum(n):
    return sum([int(i) for i in list(str(n))])

for a in range(1,lim):
    for b in range(1,lim):
        c = a**b
        digit_sum.append(get_digit_sum(c))
        # print a, '^', b, '=', c, 'sum =', s

print max(digit_sum)