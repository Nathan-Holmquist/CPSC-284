import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,4,num=100)

a = 1                                     #Replace a, b, c, d by the values produced by your programs
b = 2
c = 0                                     #Make sure that c = 0 when graphing a line
d = 0                                     #Make sure that d = 0 when graphing a line or a parabola


fx = []
for i in range(len(x)):
  fx.append( a + b*x[i] + c*x[i]**2 + d*x[i]**3 )

plt.plot(x, fx)
plt.axvline()
plt.axhline()
plt.plot([-1, 0, 1, 2, 3], [-2, 2, 1, 3, 4], 'bo')  # Plots the five given points in Questions 5-10 as blue dots
plt.show()