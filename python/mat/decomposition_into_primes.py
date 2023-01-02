from decimal import Decimal
from functools import lru_cache

@lru_cache(maxsize=None)
def SieveOfEratosthenes(n):
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n): 
		if (prime[p] == True): 
			for i in range(p * p, n+1, p):
				prime[i] = False
				p += 1
	return prime

primes = SieveOfEratosthenes(int(1e5))
while True:
	try:
		n = int(input())
		n_ = n
		assert n != 0
		values   = [0,0,0]
		c, vi, last_prime = 0, int(1e6) if n > (1e6) else n, 2
		while True:
			e = True
			for i in range(last_prime+1, vi):
				if primes[i] and n % i == 0:
						n //= i
						values[c] = i
						c+=1
						last_prime = i
						e = False
						break
			if e:
				vi = int(n**0.5)
				primes = SieveOfEratosthenes(vi)
			if c > 1:
				break
		print("{} = {} x {} x {}".format(n_,values[0],values[1],int(Decimal(n_)/(Decimal(values[1])*Decimal(values[0])))))
	except Exception as e:
		break
