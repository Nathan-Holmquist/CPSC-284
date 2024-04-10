from sympy import Matrix

# Coefficient matrix A
A = Matrix([
    [1, 1],
    [1, -1],
    [2, 1]
])

# Constants vector B
b = [5, 3, 8]
B = Matrix(b)

# Print coefficient matrix A and augmented matrix B
print("Coefficient matrix A:")
print(A)
print("\nAugmented matrix B:")
print(B)

