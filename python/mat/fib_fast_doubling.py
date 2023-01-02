# FIBONACCI FAST DOUBLING
from functools import lru_cache


def fib(n):
	if n <= 2:
		return n if n == 0 else 1
	else:
		if n & 1:  # odd
			k = (n + 1) // 2
			return (fib(k) ** 2 + fib(k - 1) ** 2)
		k = n // 2
		return ((2 * fib(k - 1) + fib(k)) * fib(k))


def fibonacci_doubling_iter(n):
	ns = []
	while n:
		ns.extend([n])
		n >>= 1

	a, b = 0, 1

	while ns:
		n = ns.pop()
		c = a * ((b << 1) - a)
		d = a * a + b * b
		if n & 1:
			a, b = d, c + d
		else:
			a, b = c, d

	return a


@lru_cache(maxsize=None)
def pis(m):
	a, b, ans = 1, 1, 1
	while True:
		buffer = b % m
		b = (a + b) % m
		a = buffer
		ans += 1
		if a == b == 1:
			return ans - 1
	return ans


print(fib(30 % 60) % 10)

while True:
	try:
		n, m = list(map(int, input().split()))
		# k = fibonacci_doubling_iter(n)
		print(pis(m))
	# print(fib(k % pis(m)) % m)
	except:
		break
