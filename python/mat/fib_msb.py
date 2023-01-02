def fib(n, m):
	msb_position = 63
	while (not ((1 << (msb_position - 1) and n)) and msb_position >= 0):
		msb_position -= 1
	a, b = 0, 1
	for i in range(msb_position, -1, -1):
		d = (a % m) * ((b % m) * 2 - (a % m) + m)
		e = (a % m) ** 2 + (b % m) ** 2
		a = d % m
		b = e % m
		if (((n >> i) & 1) != 0):
			c = (a + b) % m
			a = b
			b = c
	return a

print(fib(fib(30, 60), 10))

#print(a, 832040 % 10)
