import random
class QueensChromosome:
	def __init__(self, queens = []):
		self.__size = len(queens)
		self.__queens = queens
		self.__score = 0
		self.__init()
		
	def __init(self):
		self.__matrix = [[ 0 for j in range(self.__size)] for k in range(self.__size)]
		for j in range(len(self.__queens)):
			self.__matrix[j][self.__queens[j]] = 1
		self.__score = self.___score()

	def score(self):
		return self.__score

	def ___score(self):
		__score = 0
		for line,col in enumerate(self.__queens):
			#Verificar COLUNA!
			errors = 0
			for k in range(self.__size):
				if k!= line and self.__matrix[k][col] == 1:
					errors+=1
					break
			if line == col:
				# Diagonal principal
				for k in range(self.__size):
					for j in range(self.__size):
						if k==j and k!=line and self.__matrix[k][j] == 1:
							errors+=1
							break
			elif col == (self.__size-1)-line:
				for k in range(self.__size):
					for j in range(self.__size):
						if k==(self.__size-1)-j and k!= line:
							if(self.__matrix[k][j] == 1):
								errors+=1
								break
			else:
				#Diagonal do elemento para frente bottom-right;
				for k in range(0,abs(self.__size-(line+1))):
					if col+k+1<self.__size and line<=self.__size:
						if self.__matrix[line+k+1][col+k+1] == 1:
							errors +=1
							break
				if line>=1:
					#Diagonal do elemento para traz top-left;
					for k in range(0, line):
						if col-k-1>=0 and (line-k>=0):	
							if self.__matrix[line-k-1][col-k-1] == 1:
								errors+=1
								break
					#Diagonal do elemento para traz top-right;
					for k in range(1,abs(self.__size-col)):
						if line-k>=0 and col+k<self.__size:
							if self.__matrix[line-k][col+k] == 1:
								errors+=1
								break
				if line>=0:
					for k in range(0,abs(self.__size-(line+1))):
						if col-k-1>0:
							if self.__matrix[line+k+1][col-k-1] == 1:
								errors+=1
								break
			if errors == 0:
				__score+=1
		return __score

	def getGens(self):
		return self.__queens

	def mutate(self, multMutate=False):
		qtdMult = 1 if multMutate else random.randint(2,self.__size-1)
		gens = []
		for eta in range(qtdMult):
			gen = random.randint(0, self.__size-1)
			while  gen in gens:
				gen = random.randint(0, self.__size-1)
			gens.append(gen)
			slices = random.randint(0, self.__size-1)
			goforward = random.randint(0,1)
			if goforward==1:
				if (self.__queens[gen]+slices) > self.__size-1:
					self.__queens[gen] = (self.__queens[gen]+slices) - self.__size
				else:
					self.__queens[gen] += slices
			else:
				if (self.__queens[gen]-slices) < 0:
					self.__queens[gen] = (self.__size-1) - abs(self.__queens[gen]-slices)
				else:
					self.__queens[gen] -= slices
		self.__init()
		
	def cross(self, point, otherfather):
		son_ = []
		for k in range(point):
			son_.append(otherfather.getGens()[k])
		for k in range(point, self.__size):
			son_.append(self.__queens[k])
		son = QueensChromosome(son_)
		return son

	def __str__(self):
		return "Chromosome("+str(self.__queens)+","+ str(self.score())+")"