#rozwiąż styosując pakiet sympy układ równań liniowych
#2x1+3x2 = 4
#5x1+4x2 = 3
#naszkicuj rozwiązanie na wykresie jako punkt przecięcia obu funckji.

from __future__ import division
import sympy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import linalg as la
from scipy import optimize
sympy.init_printing()

fig ,ax = plt.subplots(figsize=(8,4))

x1 = np.linspace(-4,2,100)
x2_1 = (4-2*x1)/3
x2_2 = (3-5*x1)/4

ax.plot(x1,x2_1, 'r',lw=2,label=r"$2x_1+3x_2=0$")
ax.plot(x1,x2_2, 'b',lw=2,label=r"$5x_1+4x_2=0$")

A = np.array([[2,3],[5,4]])
b= np.array([4,3])

x = la.solve(A,b)

ax.plot(x[0],x[1],'ko',lw=2)
ax.annotate("Punkt przecięcia dwóch prostych\nroziwązanie układu równań liniowych",
            xy=(x[0],x[1]),xycoords='data',xytext=(-120,-75),textcoords='offset points',
            arrowprops = dict(arrowstyle="->",connectionstyle="arc3,rad=-.3"))

ax.set_xlabel(r"$x_1$",fontsize=18)
ax.set_ylabel(r"$x_2$",fontsize=18)
ax.legend()
fig.tight_layout()
fig.savefig('rliniowe.pdf')
plt.show()

print(f"rozwiązanie układu równań: ({x[0]},{x[1]})")
