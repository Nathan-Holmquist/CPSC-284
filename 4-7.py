import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,4,num = 100)

a = 1
b = 2
c = 0
d = 0
fx = []

for i in range(len(x)):
    fx.append( a + b*x[i] + c*x[i]**2 + d*x[i]**3 )

    plt.plot(x,fx)
    plt.axvline()
    plt.axhline()
    plt.plot([-1, 0, 1, 2, 3], [-2, 2, 1, 3, 4], 'bo')
    plt.shot()