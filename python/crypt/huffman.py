class Three:
	def __init__(self, root):
		self.__root = root
	def get_root(self):
		return self.__root
	def set_root(self,root):
		self.__root = root


class Node:
	def __init__(self,data, weight = 0):
		self.__data = data
		self.__left = None
		self.__right = None
		self.__weight = weight
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
		pass
	def __cout_letters(self,word):
		unique_words = {}
		for letter in list(word):
			if unique_words.get(letter) is None:
				unique_words[letter] = 1 # Inicia a contagem da letra caso seja a primeira ocorrencia dela
			else:
				unique_words[letter] += 1 # Incrementa a ocorrencia
		return unique_words
		
	def __mout_tree(self,unique_words):
		# Monta uma arvore binaria a partir de um dicionario de ocorrencia de letras
		aux_vector = sorted(unique_words.items(),key=lambda e: e[1])
		nodes = [Node(k,weight=v) for k,v in aux_vector]
		while(len(nodes)>1):
			nodeTemp = Node(None, nodes[0].weight()+nodes[1].weight())
			nodeTemp.set_right(nodes[0])
			nodeTemp.set_left(nodes[1])
			nodes.remove(nodes[0])
			nodes.remove(nodes[0])
			nodes.append(nodeTemp)
			nodes = sorted(nodes,key=lambda e: e.weight())
		three = Three(nodes[0])
		return three
	def encrypt(self, data):
		print("Palavra: {}".format(data))
		three = self.__mout_tree(self.__cout_letters(data))
		return three

if __name__ == "__main__":
	hf = HuffmanAlgorithm()
	hf.encrypt("Batata")