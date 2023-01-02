import math, random
import numpy as np

class ActivationFunctions:
	class Tanh:
		@staticmethod
		def f_x(u):
			return math.tanh(u)
		@staticmethod
		def f__x(u):
			return math.pow(1/math.cosh(u),2)
	class Sigmoid:
		@staticmethod
		def f_x(u):
			return 1/(1 + math.exp(-u))
		@staticmethod
		def f__x(u):
			try:
				return (math.exp(u)/math.pow((1+math.exp(-u)),2))
			except:
				return 0

class Perceptron:

	def __init__(self, size = 3, learn_cfg = 0.01, activation_fn = ActivationFunctions.Tanh):
		self.__size = size
		self.__learn_cfg = learn_cfg
		self.__activation_fn = activation_fn
		self.__weights = np.array([ random.random() for j in range(size+1)])
	def predict(self, input):
		u = np.dot(np.array(self.__weights).T, input)
		return self.__activation_fn.f_x(u)
	# TREINAMENTO PELO GRADIENTE DESCENDENTE E ERRO MEDIO QUADRATICO.
	def cost(self,outputs, inputs):
		e = 0
		for index, input in enumerate(inputs):
			e += math.pow(outputs[index]- np.dot(self.__weights.T, input),2)
		return e/len(inputs)


	def learn(self, data = [], inputs = [], max_epochs = 50000 , err = 4e-2 ):
		inputs = np.array(list(map(lambda e: np.array([1]+e), inputs)))
		for epoch in range(max_epochs):
			cost = self.cost(data, inputs)
			if cost < err:
				print("Precisão alcancada...")
				break
			if epoch % 100 == 0 :
				print("Epoca {} erro medio quadratico atual {}".format(epoch, cost))
			# ATUALIZAR PESOS
			for j in range(len(self.__weights)):
				oldWeight = self.__weights[j]
				error = 0
				for index,input in enumerate(inputs):
					u = np.dot(self.__weights.T, input)
					error+= (data[index] - self.predict(input))*self.__activation_fn.f__x(u)*input[j]
				newWeight = oldWeight + (2/len(inputs))*self.__learn_cfg*error
				self.__weights[j] = newWeight

		for index,input in enumerate(inputs):
			print("Esperado: {}, saida: {}, inputs: {} ".format(data[index], round(self.predict(input)), input ))
		print("Esperado: {}, saida: {}, inputs: {} ".format(0, round(self.predict([1,0,0])), [1,0,0]))


if __name__ == "__main__":
	neuron =  Perceptron(size=2)
	dataset_outputs = [1,0,0]
	dataset_inputs = [[1,1], [0,1], [1,0]]
	neuron.learn(dataset_outputs, dataset_inputs, max_epochs=100000)