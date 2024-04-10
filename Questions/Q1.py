from sympy import *                                         #This makes the rref() function available
from sympy.interactive.printing import init_printing        #This is for formatting of matrices
import math                                                 #For square roots

A = Matrix([[1,1],[1,-1],[2,1]])                           #A is a coefficient matrix for a linear system
print("Coefficient Matrix A:")                                                          #Prints the matrix A
print(A)


b = Matrix([[5],[3],[8]])                                  #column matrix b for the system Ax=b                                   #prints matrix b



AugA = A.row_join(b)                                        #Forms the augmented matrix [A|b]  (Make sure b has the same number of rows as A)
print("Augmented Matrix: ")
print(AugA)


D = AugA.rref()                                             #reduced row echelon form for AugA
print("Reduced Row Echelon form for AugA: ")                                           #Prints the matrix D (without info about columns with leading 1's)
print(D[0])


AT = A.transpose()                                          #Transpose of matrix A
print("Transpose of matrix A: ")
print(AT)


AugAT = AT*AugA                                             #AT multiplied by the augmented matrix for the original system
print("AT multiplied by the augmented matrix for the original system:")
print(AugAT)


D = AugAT.rref()                                            #Converts the new augmented matrix into reduced row echelon form
print("New matrix converted into RREF:")
print(D[0])

