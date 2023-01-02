import re, array, json, math, sys, time

class Three:
	def __init__(self, root):
		self.__root = root
		self.__size = 0
	def root(self):
		return self.__root

	def set_root(self, root):
		self.__root = root
	def set_size(self, size):
		self.__size = size


class Node:
	def __init__(self,data, weight = 0):
		self.__data = data
		self.__left = None
		self.__right = None
		self.__weight = weight
	def data(self):
		return self.__data
	def right(self):
		return self.__right
	def left(self):
		return self.__left
	def set_right(self,node):
		self.__right = node
	def set_left(self,node):
		self.__left = node
	def __str__(self):
		return "Node<{},{}>".format(self.__data, self.__weight )
	def set_weight(self,weight):
		self.__weight = weight
	def weight(self):
		return self.__weight

class HuffmanAlgorithm:
	def __init__(self):
		self.__dict = {}
		self.__keys = []
		self.__three = None
	def __cout_letters(self,word):
		# Conta a ocorrencia das letras
		unique_letters = {}
		for letter in word:
			if letter not in unique_letters:
				unique_letters[letter] = 0 # Inicia a contagem da letra caso seja a primeira ocorrencia dela
			unique_letters[letter] += 1 # Incrementa a ocorrencia
		return unique_letters
		
	def __mout_three(self,unique_words):
		# Monta uma arvore binaria a partir de um dicionario de ocorrencia de letras
		aux_vector = sorted(unique_words.items(),key=lambda e: e[1]) 
		self.__keys = unique_words.keys()
		nodes = [Node(k,weight=v) for k,v in aux_vector]
		nodes_size = len(nodes)
		while(len(nodes)>1):
			nodeTemp = Node(None, nodes[0].weight()+nodes[1].weight())
			nodeTemp.set_right(nodes[0])
			nodeTemp.set_left(nodes[1])
			nodes.remove(nodes[0])
			nodes.remove(nodes[0])
			nodes.append(nodeTemp)
			nodes_size+=1
			nodes = sorted(nodes,key=lambda e: e.weight())
		three = Three(nodes[0])
		self.__three = three
		three.set_size(nodes_size)
		return three

	# Transformar iterativo....
	def __get_symbol_value(self, symbol, node, binvalue = ""):
		if node is not None:
			if symbol  in self.__dict:
				return self.__dict[symbol]
			else:
				if node.data() == symbol:
					self.__dict[symbol] = binvalue
					return binvalue
				else:
					self.__get_symbol_value(symbol, node.left(), binvalue+"0")
					self.__get_symbol_value(symbol, node.right(), binvalue+"1")
	def __mout__dict(self, three):
		for letter in self.__keys:
			self.__get_symbol_value(letter,three.root())
		self.__dec_dict = {v: k for k, v in self.__dict.items()} #dicionario invertido
		self.__serializable_dict = list(format(ord(x),'08b') for x in json.dumps(self.__dec_dict).replace(" ,", ",").replace(", ", ","))
	def encrypt(self, data):
		self.__mout_three(self.__cout_letters(data))
		self.__mout__dict(self.__three)
		binary = "".join(map(lambda e: self.__dict[e], data))
		return binary
	def encrypt_file(self, filename):
		with open(filename, "r") as pointer:
			data = "".join(pointer.readlines())
			bits = self.encrypt(data)
			last_byte_usage =   format(len(bits)%8,"08b")
			bin_array = array.array("B")
			len_dict = "{0:b}".format(len(self.__serializable_dict))
			bin_len = "0"*(32 - len(len_dict)) + len_dict
			dict_bin = "".join(self.__serializable_dict)
			bits = bin_len + last_byte_usage + dict_bin + bits
			for j in range(0,len(bits), 8):
				if(len(bits[j:j+8]) != 8):
					subs = "0"*(8-len(bits[j:j+8])) + bits[j:j+8]		
					bin_array.append(int(subs, 2))
				else:
					bin_array.append(int(bits[j:j+8], 2))
			with open("".join(filename.split(".")[:-1]+[".titanxd"]), "wb+") as f:
				try:
					b_array = bytes(bin_array)
					f.write(b_array)
					print("Arquivo salvo com sucesso....")
				except:
					print("Erro ao salvar...")
	def decrypt(self, data):
		original_data = ""
		bitSum = ""
		for bit in data:
			bitSum += bit
			if bitSum in self.__dec_dict:
				original_data += self.__dec_dict[bitSum]
				bitSum = ""
		return original_data
	def decrypt_file(self, filename, new_name="data.txt"):
		with open(filename, "rb") as pointer:
			b_array = pointer.readlines()
			int_array = []
			for j in b_array:
				int_array += j
			b_array = int_array
			len_dict = "".join(list(map(lambda e :format(e, "08b"),b_array[0:4])))
			len_dict = int(len_dict,2)
			lsb =  int("".join(list(map(lambda e :format(e, "08b"),b_array[4:5]))),2)
			__dict = "".join(list(map(chr,b_array[5:len_dict+5])))
			__dict = json.loads(__dict)
			self.__dec_dict = __dict
			if lsb>0:
				new_data = b_array[len_dict+5:-1]
				dec_data = self.decrypt(  "".join(list(map(lambda e : format(e,"08b") , new_data)))  + format(b_array[-1],"08b")[8-lsb:]  )
			else:
				new_data = b_array[len_dict+5:]
				print(len_dict)
				dec_data = self.decrypt("".join(list(map(lambda e : format(e,"08b") , new_data))))
			with open(new_name,"w+") as f:
				try:
					f.writelines(dec_data)
					print("Arquivo descompactado com sucesso")
				except:
					print("Erro ao salvar")
if __name__ == "__main__":	
	hf = HuffmanAlgorithm()
	hf.encrypt_file("huffman.py")
	time.sleep(1)
	print("Descompactando...")
	hf.decrypt_file("huffman.titanxd", "huffman-2.json")