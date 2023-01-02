import numpy as np
from matplotlib import pyplot as plt

def iTR(Y, dh):
    return (dh/2)*sum([Y[0],Y[-1], *list(map(lambda e: 2*e, Y[1:-1]))])
def iSR(Y, dh):
    return (dh/3)*sum([Y[0], Y[-1], 4*sum([ y for i , y in enumerate(Y[1:-1]) if i % 2 == 0 ]), 2*sum([ y for i , y in enumerate(Y[2:-2]) if i % 2 == 0 ])])

def diff(fx, x0, dx):
    return (fx(x0 + dx) - fx(x0) )/dx


def sin(x):
    return np.sin(x)

dx = 0.0001
X = np.linspace(0, 2*np.pi, 1000)
y = -np.sin(X)
y_ = diff(np.cos, X, dx)

plt.plot(X,y, 'r')
plt.plot(X,y_,'b')
plt.show()



print(diff(sin, 0.1, 0.0001))
print(np.cos(0.1))