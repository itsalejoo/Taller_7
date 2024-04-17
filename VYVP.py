#imprimimos la biblioteca numpy y le ponemos el alias np
import numpy as np

# Definimos una matriz nxn en este caso 3x3 
A = np.array([[2, 3, 6], [9, 12, 18], [11, 8, 6]])

# Calculamos los vectores y valores propios
#llamamos la función np.linalg.eig que se utiliza para calcular los valores propios y vectores propios de una matriz cuadrada determinada.
eigenvalues, eigenvectors = np.linalg.eig(A)

# mostramos los valores propios 
print("valores propios:")
print(eigenvalues)

# mostramos los vectores propios 
print("vectores propios:")
print(eigenvectors)