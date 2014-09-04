coins = [1,2,5,10,50,100,200]
coins.reverse()
t = coins[0]
count = 1 # 200 piece first


level=1
coin = coins[level]
div = t/coin	
if div > 1:
	count+=1
else:
	count+=div
	level+=1
	coin = coins[level]
	i = 0
	while i < div:
		change = change - i*coin
		
			
		
		
		
