alpha = "abcdefghijklmnopqrstuvwxyz"
n = int(input())
encode_ = []
def encode(word):
	temp = []
	for k in word:
		if k.lower() in alpha:
			temp.append(chr(ord(k)+3))
		else:
			temp.append(k)
	tp2 = []
	tp_word = ''.join(temp)[::-1] 
	for i,k in enumerate(tp_word):
		if i >= int(len(tp_word)/2):
			tp2.append(chr(ord(k)-1))
		else:
			tp2.append(k)
	return ''.join(tp2)
for k in range(n):
	word = input()
	encode_.append(encode(word))
for z in encode_:
	print(z)