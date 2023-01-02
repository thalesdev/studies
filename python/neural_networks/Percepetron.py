import numpy as np
import scipy as sp, sympy as syp
import json
from matplotlib import pyplot as pp


class Activation:
    def __init__(self, tp = "relu"):
        self.type = tp
    def __relu__(self,x):
        return np.round(np.maximum(x, 0),4)
    def __elu__(self,x, alpha = 0.5):
        return x if x > 0 else alpha*(np.e**x - 1) 
    def __leaky_relu__(self, x, alpha = 0.01):
        return x if x > 0 else alpha**x
    def __sigmoide__(self, x, alpha = 1, beta = 1):
        return 1/(1 + alpha*(np.e**(-beta*x)))
    def __linear__(self, x):
        return x 

    def call(self):
        return getattr(self, "__"+self.type+"__")
        
class Percepetron:
    def __init__(self, axis = 3, activation = None):
        self.__axis = axis
        self.__activation = activation
        self.__weights = np.random.random((axis+1,))
    def __integrate(self, input):
        return (self.__weights[1:].T).dot(input) + self.__weights[0]
    def predict(self, inputs):
        return self.__activation.call()( self.__integrate(inputs) )
    def fit(self,dataset=[], outputs = [],  epochs = syp.oo , alpha = 0.01):
            error = True
            epoch = 0
            while error:
                error = False
                for index, sample in enumerate(dataset):
                    output = outputs[index]
                    y_estimated = self.predict(sample)
                    err = output - y_estimated
                    sp = np.ones(self.__axis+1)
                    sp[1:]*=sample
                    sample = sp
                    if err != 0:
                        self.__weights += alpha*err*sample 
                        error = True
                epoch+=1
                if epochs != syp.oo:
                    if epoch == epochs:
                        break
            return True
    def __str__(self):
        return "Weights : {}".format(self.__weights)
    

    def plot(self, payload):
        if self.__axis == 2:
            for x,y in payload:
                pp.plot(x,y,color="r", marker='o')
            x= np.linspace(0, 1)
            y = (-x*self.__weights[2] - self.__weights[0])/self.__weights[1]  
            plt, = pp.plot(x, y)
            pp.xlabel(r"$X_2$")
            pp.ylabel(r"$X_1(x_2,\beta)$")
            pp.legend( (plt,), (r"$W_1 \approx {} , W_2 \approx {}$".format(*np.round(self.__weights[1:])),))
            pp.title("Perceptron Single Layer 2D")
            pp.show()


pcp = Percepetron(2, Activation("relu")) # And
#dataset = np.loadtxt("southampton_precip.txt")
outputs = np.array([1,0,0,0])
inputs = np.array([[1,1],[1,0],[0,0],[0,1]])
pcp.fit(inputs, outputs, alpha=0.08)
pcp.plot(inputs)
#print(pcp)