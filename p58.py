from primes import Primes

n = i = 1
p = Primes()
percent = 1

diagonals = 1 # this takes into account the center (1)
prime_diagonals = 0

while percent > 0.1:
    for x in range(4):
        n+=2*i  
        prime_diagonals += p.is_prime(n)
    diagonals += 4    
    i+=1
    percent = float(prime_diagonals) / diagonals
    print prime_diagonals, '/', diagonals, ',', percent

print 'side =', int(n**(0.5)), 'primes =', prime_diagonals, '/', diagonals, percent