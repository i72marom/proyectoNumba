import numba

@numba.jit
def determinanteNumba(m, n):
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

def determinante(m, n):
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