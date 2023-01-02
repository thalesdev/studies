import math
maior_cadeia = 0
def partir(a,b):
	global maior_cadeia
	tamanho = len(a)
	#print(a)
	if a in b:
		if maior_cadeia < tamanho:
				maior_cadeia = tamanho
	else:
		if tamanho == 1:
			if a in b:
				if maior_cadeia < tamanho:
					maior_cadeia = 1
			return 0
		else:
			if tamanho %2  ==0 and tamanho != 2:
				metade = int(tamanho/2)
				a_1 = a[:metade+1]
				a_2 = a[metade-1:]
			elif tamanho ==2:
				a_1 = a[0]
				a_2 = a[1]				
			else:				
				metade = int(math.ceil(tamanho/2))
				a_1 = a[:metade-1]
				a_2 = a[metade-1:]
			partir(a_1,b)
			partir(a_2,b)
	return 0
while True:
	try:
		str1 = input().lower()
		str2 = input().lower()
		partir(str2,str1)
		partir(str1,str2)
		print(maior_cadeia)
		maior_cadeia = 0
	except EOFError:
		break