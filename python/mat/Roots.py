# coding:utf-8

"""
	Metodos de achar raizes de funções numericamente
"""


def bolzano(f, f_):
	return f * f_ < 0


def arange(x, y, step=1):
	yield x
	while x + step < y:
		yield round(x + step, 13)
		x += step


def colario(arange, del_f):
	for i, x in enumerate(arange):
		if i == 0:
			signal = 1 if del_f(x) > 0 else 0
		else:
			if (signal and del_f(x) < 0) or (not signal and del_f(x) > 0):
				return False
	return True


def range_root(f, dfdx, arange):
	x = list(arange)
	y = list(map(f, x))
	i, (a, b) = 0, (0, len(x) - 1)
	while i < b:
		j = b
		while j > a and i != j:
			if bolzano(y[i], y[j]) and colario(x[i:j + 1], dfdx):
				yield x[i], x[j]
				i = j - 1
				break
			j -= 1
		i += 1


def newton_raphson(f, df, x0, epsilon, max_iter=1000):
	for i in range(max_iter):
		fx = f(x0)
		if abs(fx) < epsilon:
			return x0
		delf = df(x0)
		assert delf != 0, "Não Existe Soluções Para Essa Função, Derivada Nula!"
		x0 -= fx/delf
	raise Exception("Nenhuma solução encontrada.")



def bisection(f, a,b, epsilon, max_iter=100):
	assert f(a)*f(b) < 0, "Não existe uma raiz nesse intervalo!"
	def signal(x):
		return x > 0
	for i in range(max_iter):
		c = a + (b-a)/2
		if f(c) == 0 or abs(((b-a)/2)) < epsilon:
			return c
		if f(a)*f(c) > 0 :
			a = c 
		else:
			b = c
	raise Exception("Nenhuma Solução Encontrada.")

def bisection_beteween_ranges(f, delf, arange, epsilon, max_iter=1000):
	for (a,b) in range_root(f, delf, arange):
		for i in range(max_iter):
			try:
				xn = bisection(f, a,b, epsilon, max_iter=max_iter)
				yield xn
				break
			except:
				pass




def gaussjacobi(a,b,p):
	n = len(a)
	alphas = [sum(map(lambda el: abs(el[1]),filter(lambda e : e[0] != i ,enumerate(a[i]))))/abs(a[i][i]) for i in range(n)]
	#print(alphas)
	if max(alphas) > 1:
		raise Exception("O metodo não converge")
	x0 = [0 for i in range(n)]
	k = 0
	err = True
	while True:
		for i in range(n):
			pass









#a = [[9,-1,2], [5,7,2], [-3,3,7]]
#b = [1,0,2]
#p = 1e-3

#gaussjacob(a,b,p)