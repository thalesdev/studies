precos = [1,5,8,9,10,17,17,20,22,24,26,28,30,30] + list(range(32,50,3))
melhor_receita  = {}
melhor_receita2 = {}
melhor_pedacos = {}
def renda(k):
	global melhor_receita
	if k == 1 or k == 0:
		melhor_receita[k] = k
	elif melhor_receita.get(k) is None:
		r_max = 0
		for j in range(1,k+1):
			r_temp = precos[j-1] + renda(k-j)
			if r_temp > r_max:
				r_max = r_temp
		melhor_receita[k] = r_max
	return melhor_receita[k]


def renda_it(k):
	global melhor_receita2
	global melhor_pedacos
	melhor_receita2[0] = 0
	melhor_receita2[1] = precos[0]
	melhor_pedacos[0] = [0]
	melhor_pedacos[1] = [1]
	for y in range(2,k+1):
		r_max = 0
		pedacos_max = None
		for j in range(y,0,-1): 
			r_temp = precos[j-1] + melhor_receita2[y-j]
			if r_temp > r_max:
				r_max = r_temp
				pedacos_max = [j,y-j] if 0 != y-j else [j] 
		melhor_receita2[y] = r_max
		melhor_pedacos[y] = pedacos_max 
	return melhor_receita2[k]


#renda(20)
renda_it(8)
print(melhor_receita2)
print(melhor_pedacos)
#print(melhor_receita2)