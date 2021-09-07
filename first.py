import numpy as np
from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt

x, d1, d2 = symbols('x d1 d2')
eq1 = Eq((x-d1)**2+(0.4**2)-(2**2)*(d1**2),0)
sol11 = solve(eq1,d1)
d11 = sol11[1]
eq2 = Eq((2*d11+d2-x)**2+(0.7**2)-(2**2)*(d2**2),0)
sol21 = solve(eq2,d2)
d21 = sol21[1]
t1 = 2*(d11+d21)

eq1 = Eq((x-d1)**2+(0.7**2)-(2**2)*(d1**2),0)
sol12 = solve(eq1,d1)
d12 = sol12[1]
eq2 = Eq((2*d12+d2-x)**2+(0.4**2)-(2**2)*(d2**2),0)
sol22 = solve(eq2,d2)
d22 = sol22[1]
t2 = 2*(d12+d22)
delta = t1-t2

xx = []
yy = []
for i in range(50 , 150 , 1):
    d = delta.subs(x, i/100)
    yy.append(d)
    xx.append(i/100)
root = [15] 
plt.plot(xx,yy,markevery=root,marker="o")
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$\delta (x)$')
plt.show()  
