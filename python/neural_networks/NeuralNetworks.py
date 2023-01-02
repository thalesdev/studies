import random, math
class ActivationFunciton:
	b = 1
	@staticmethod
	def tanh(v):
		return math.tanh(v)
	@staticmethod
	def sigmoidal(v):
		return (1/1+math.exp(-v*ActivationFunciton.b))
	@staticmethod
	def heaveside(v):
		if v>=lim_sup:
			return 1
		else:
			return -1
	def dtanh(v):
		return (1/math.cosh(v))**2
	def dsigmoidal(v):
		return ((ActivationFunciton.b*math.exp(ActivationFunciton.b*v))/((1+math.exp(v*ActivationFunciton.b))**2))

class Perceptron:
	"""docstring for ClassName"""
	def __init__(self, num_inputs=2, learn_cfg=0.05, activation_fn=ActivationFunciton.sigmoidal):
		self.__weight = [0 for j in range(num_inputs)]
		self.__inputs = [None for j in range(num_inputs)]
		# BIAS (LIMIAR)
		#self.__weight[0] = random.random()
		#self.__inputs[0] = -1
		self.__learn_cfg = learn_cfg
		self.__size = num_inputs
		self.__acv_fn = activation_fn
	def predict(self,inputs):
		v=0
		for j,signal in enumerate(inputs):
			v += signal*self.__weight[j]
		return self.__acv_fn(v)

	def weights(self):
		return self.__weight
	def setWeights(self, weights):
		self.__weight = weights
	def derivative(self, v):
		if self.__acv_fn == ActivationFunciton.tanh:
			return ActivationFunciton.dtanh(v)
		elif self.__acv_fn == ActivationFunciton.sigmoidal:
			return ActivationFunciton.dsigmoidal(v) 
	def __str__(self):
		return "{}".format(len(self.__inputs))		

class PerceptonMultiLayer:
	def __init__(self, layers=(1,2,1), num_inputs=3,learn_cfg=0.001):
		if len(layers) < 2:
			raise Exception("Não é uma rede multlayer.")
		self.__num_layers = len(layers)
		self.__num_inputs = num_inputs
		self.__learn_cfg = learn_cfg
		self.__tp_layers = layers
		self.__layers = [[Perceptron(num_inputs= num_inputs if key == 0 else layers[key-1]) for k in range(j)] for key,j in enumerate(layers)]
	def predict(self, input):
		x = input
		outputs = []
		for k,v in enumerate(self.__layers):
			outputs.append([])
			for neuron in v:
				if k==0:
					y_n = neuron.predict(x)
				else:
					y_n = neuron.predict(outputs[k-1])
				outputs[k].append(y_n)
		return outputs[-1]
	def __broadcast(self, input):
		x = input
		outputs = []
		for k,v in enumerate(self.__layers):
			outputs.append([])
			for neuron in v:
				if k==0:
					y_n = neuron.predict(x)
				else:
					y_n = neuron.predict(outputs[k-1])
				outputs[k].append(y_n)
		return outputs
	# FAIL
	def training(self, inputs , outputs, epochs=50000):
		epoch = 0
		error = False
		deltas = [[0 for i in range(j)] for j in self.__tp_layers] 
		while(epoch < epochs and not error):
			error = True
			for vv,j in enumerate(inputs):
				# Propagação
				x = j
				outputs_x = self.__broadcast(x)
				y_fn = outputs_x[-1]
				for c,(k1,k2) in enumerate(zip(y_fn, outputs[vv])):
					if k1!=k2:
						delta = k1-k2
						deltas[-1][c] = delta
						error = False
				print(deltas)
				# Retro Propagação
				# Calculando deltas
				#print(len(self.__layers)-1,0,-1)

				for i in range(len(self.__layers)-2,-1,-1):
					for id, neuron in enumerate(self.__layers[i]):
						s = 0 
						for idw,n in enumerate(self.__layers[i+1]):
							s += n.weights()[id]*deltas[i+1][idw]
						deltas[i][id] = s
				#print(deltas)
				# Calculando novos pesos
				for i, layer in enumerate(self.__layers):
					for id,neuron in enumerate(layer):
						w = []
						for idw,weight in enumerate(neuron.weights()):
							v = 0
							for ij, nn in enumerate(self.__layers[i]):
								weig= nn.weights()[idw]
								v+= weig*outputs_x[i][ij]
							w_ = weight + self.__learn_cfg*neuron.derivative(v)*deltas[i][id]
							w.append(w_)
						#print("weighsts",w)
						neuron.setWeights(w)
				#error = True
			epoch+=1
			#print("epoch ",epoch)
		print(self.predict(inputs[0]))
		print("acabou o treinamneto ",epoch)