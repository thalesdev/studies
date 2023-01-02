def dec_to_bin(dec):
	bin = ""
	while(dec>=1):
		bin+= str(dec%2)
		dec//=2
	return str(bin)
def dec_compl_2(dec, nbits = 8):
	if dec>0:
		if dec <= (2**nbits)-1:
			binary = dec_to_bin(dec)
			return  str(binary + ("0"*(nbits-len(binary))))[::-1]
	else:
		if abs(dec) <= (2**nbits):
			binary = dec_to_bin(abs(dec+1))
			binary =   binary + ("0"*(nbits-len(binary)))
			return "".join(list(map(lambda e: "1" if e == "0" else "0", list(binary)[::-1])))
	raise Exception("This number is not representable..  Range[{},{}]".format(-2**nbits, (2**nbits)-1))
def sum_two_compl(x,y,nbits=8):
	x,y, result, carry_on = x[::-1],y[::-1],[],0
	#print(x[::-1],"\n",y[::-1])
	for (x_,y_) in zip(x,y):
		res = int(x_)+int(y_)+carry_on
		#print(res, x_,y_, carry_on)
		if res==2:
			result.append(0)
			carry_on=1
		elif res==3:
			result.append(1)
			carry_on=1
		else:
			result.append(res)
			carry_on = 0
	#print(result)
	return "".join(list(map(str,result[::-1])))
def move_without_signal(x):
	new_number = [] # Signal
	for j in x[-2::-1]:
		new_number.append(j)
	new_number.append(x[0])
	return new_number[::-1]
def compl_2_dec(compl):
	result = 0
	for ind, val in enumerate(compl[::-1]):
		result+= (-2**ind if ind == len(compl)-1 else 2**ind ) if val == "1" else 0
	return result
def booth(x,y, nbits=8):
	if (y>x):
		a = y
		y = x
		x = a
	if x == 0 or y == 0:
		return "0"*nbits 
	x_ = dec_compl_2(x,nbits=nbits)
	x__ = dec_compl_2(-x,nbits=nbits)
	y_ = dec_compl_2(y,nbits=nbits)
	limit_negative = (-2**(nbits-1) == x) or (y == -2**(nbits-1))
	A = [ x_[j] for j in range(nbits)] + ["0" for j in range(nbits)] + ["0"]
	A = ["0"] +  A if limit_negative else A
	S = [ x__[j] for j in range(nbits)] + ["0" for j in range(nbits)] + ["0"]
	S = ["0"] +  S if limit_negative else S	
	P = [ "0" for j in range(nbits)] + [ y_[j] for j in range(nbits) ] + ["0"]
	P = ["0"] +  P if limit_negative else P	
	print("#"*40,"\nA INICIAL={}\nS Inicial={}\nP Inicial={}".format(A,S,P))
	for j in range(nbits):
		end = P[-2:]
		if (["0","0"] != end) and (["1","1"] != end):
			if ["0","1"] == end:
				print("P = P+A\n P={}\nA={}".format(P,A))
				P = sum_two_compl(P,A)
			else:
				print("P = P+S\nP={}\nS={}".format(P,S))
				P = sum_two_compl(P,S)
		print("Antes de mover : P=", "".join(P))
		P = move_without_signal(P)
		print("Depois de mover : P=", "".join(P))
	return "".join(P[:-1])
while True:
	print("-"*100)
	x = int(input("Digite um numero [-16,15):"))
	y = int(input("Digite um numero [-16,15):"))
	r = booth(x,y,5)
	print("Valor binario = {}\nresultado= {}\nresultado esperado= {}".format(r, compl_2_dec(r), x*y))