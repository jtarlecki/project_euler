def factorial(n):
	f = i = 1
	while not i > n:
		f*=i
		i+=1
	return f

lim = 10**6
i = 3
ans =[]

while i < lim:
	strings = list(str(i))
	f_sum = 0
	for string in strings:
		f_sum += factorial(int(string))
		if f_sum == i:
			ans.append(i)
	i+=1
	
print sum(ans)