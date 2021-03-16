import numba
import numpy

@numba.jit
def determinanteIterNumba(m, n):
	aux = 0.0
	det = 1

	for k in range(0, n-1):
		det *= m[k][k]
		
		if m[k][k] == 0: return 0
		else:
			for i in range(n+1, n):
				aux = -m[i][k]

				for j in range(k, n):
					m[i][j] = m[i][j] + aux * m[k][j] / m[k][k]

	return det * m[n-1][n-1]

def determinanteIter(m, n):
	aux = 0.0
	det = 1

	for k in range(0, n-1):
		det *= m[k][k]
		
		if m[k][k] == 0: return 0
		else:
			for i in range(n+1, n):
				aux = -m[i][k]

				for j in range(k, n):
					m[i][j] = m[i][j] + aux * m[k][j] / m[k][k]

	return det * m[n-1][n-1]

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
