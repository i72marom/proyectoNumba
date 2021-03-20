import numba
import numpy

"""
 * Calcula el determinante de una matriz. Esta función se compila con numba.
 *
 * m: Matriz de orden n
 * n: orden de la matriz
"""
@numba.jit
def determinanteIterNumba(m, n):
	aux = 0.0
	det = 1

	for k in range(0, n-1):
		det *= m[k][k]
		
		if m[k][k] == 0: return 0
		else:
			for i in range(k+1, n):
				aux = -m[i][k]

				for j in range(k, n):
					m[i][j] = m[i][j] + aux * m[k][j] / m[k][k]

	return det * m[n-1][n-1]

"""
 * Calcula el determinante de una matriz. Esta función se ejecuta directamente con el interprete.
 *
 * m: Matriz de orden n
 * n: orden de la matriz
"""
def determinanteIter(m, n):
	aux = 0.0
	det = 1

	for k in range(0, n-1):
		det *= m[k][k]
		
		if m[k][k] == 0: return 0
		else:
			for i in range(k+1, n):
				aux = -m[i][k]

				for j in range(k, n):
					m[i][j] = m[i][j] + aux * m[k][j] / m[k][k]

	return det * m[n-1][n-1]

"""
 * Calcula el determinante de una matriz de forma recursiva. Esta función se compila con numba.
 *
 * m: Matriz de orden n
 * n: orden de la matriz
"""
@numba.jit
def detRecursivoNumba(m, n):
	if n == 1: return m[0][0];
	
	f = 1;
	det = 0;

	for i in range(0,n):
		sub_m = numpy.zeros((n-1,n-1))
		
		for j in range(0,n-1):
			for k in range(0,n-1):
				if k < i:  sub_m[j][k] = m[j+1][k];
				if k >= i: sub_m[j][k] = m[j+1][k+1];

		det += f * m[0][i] * detRecursivoNumba(sub_m, n-1);
		f *= -1;

	return det

def detRecursivo(m, n):
	if n == 1: return m[0][0];
	
	f = 1;
	det = 0;

	for i in range(0,n):
		sub_m = numpy.zeros((n-1,n-1))
		
		for j in range(0,n-1):
			for k in range(0,n-1):
				if k < i:  sub_m[j][k] = m[j+1][k];
				if k >= i: sub_m[j][k] = m[j+1][k+1];

		det += f * m[0][i] * detRecursivo(sub_m, n-1);
		f *= -1;

	return det

"""
 * Calcula el producto de dos matrices. Esta función se compila con numba.
 *
 * A: Matriz de orden n
 * B: Matriz de orden n
"""
@numba.jit
def productoMatrizNumba(A, B):
	n         = len(A)
	resultado = numpy.zeros((n,n))

	for i in range(0,n):
		for j in range(0,n):
			for k in range(0,n):
				resultado[i][j] = A[i][k] * B[k][j]

	return resultado

"""
 * Calcula el exponente de una matriz. Esta función se compila con numba.
 *
 * m: Matriz de orden n
 * n: orden de la matriz
"""
@numba.jit
def exponenteMatrizNumba(m, n, exp = 30):
	resultado = numpy.zeros((n,n))

	resultado = productoMatrizNumba(m, m)
	for x in range(3,exp):
		resultado = productoMatrizNumba(m, resultado)

"""
 * Calcula el producto de dos matrices. Esta función se ejecuta directamente con el interprete.
 *
 * A: Matriz de orden n
 * B: Matriz de orden n
"""
def productoMatriz(A, B):
	n         = len(A)
	resultado = numpy.zeros((n,n))

	for i in range(0,n):
		for j in range(0,n):
			for k in range(0,n):
				resultado[i][j] = A[i][k] * B[k][j]

	return resultado

"""
 * Calcula el exponente de una matriz. Esta función se ejecuta directamente con el interprete.
 *
 * m: Matriz de orden n
 * n: orden de la matriz
"""
def exponenteMatriz(m, n, exp = 30)):
	exp = 30
	resultado = numpy.zeros((n,n))

	resultado = productoMatriz(m, m)
	for x in range(3,exp):
		resultado = productoMatriz(m, resultado)
