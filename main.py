from sympy import *
from sympy.interactive.printing import init_printing
import math

A = Matrix([[2,-1],[1,3],[5,1]])
print(A)

b = Matrix([[5],[2],[4]])
print(b)

AugA = A.row_join(b)
print(AugA)

D = AugA.rref()
print(D[0])

AT = A.transpose()
print(AT)

AugAT = AT*AugA
print(AugAT)

D = AugAT.rref()
print(D[0])

