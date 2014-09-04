limit = 100
sum_of_squares = 0
sum_digits = 0

# sum of squares
for i in range(1, limit+1):
    sum_of_squares += i**2
    sum_digits += i

square_of_sum = sum_digits**2

diff = square_of_sum - sum_of_squares

print 'sum_of_squares = ', sum_of_squares
print 'square_of_sum = ', square_of_sum

print 'diff = ', diff