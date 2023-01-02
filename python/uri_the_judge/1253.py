num_tests = int(input())
start = 65
end = start+26
encodes = []
def encode (text, translate):
	chunks = []
	for chunk in text:
		l = ord(chunk)-translate if ((ord(chunk)-translate) >= start) else end - ( translate - (ord(chunk) - start)) 
		chunks.append(chr(l))
	return ''.join(chunks)  
for k in range(num_tests):
	text =  input()
	nCiph = int(input())
	encodes.append(encode(text,nCiph))
for k in encodes:
	print(k)
