while True:
	try:
		odds, evens = [], []
		for i in range(int(input())):
			val = int(input())
			if val&1:
				odds.append(val)
			else:
				evens.append(val)
		print(*sorted(evens), sep='\n')
		print(*sorted(odds, reverse=True), sep='\n', end='\n')
		
	except:
		break
