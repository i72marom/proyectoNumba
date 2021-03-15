import numpy
import numba
from time import time
import algoritmos as a
import random

def escribeFichero(lista, nombre):
	f = open("txt/" + nombre + ".txt", "w")
	
	for i in lista: 
		f.write(str('{:,.15f}'.format(i)) + "\n")

	f.close()

def imprimeAyuda():
	ayuda_ = "Opciones: \n\t0. Salir. \n\t1. Ayuda. \n\t2. Determinante iterativo\n"
	print(ayuda_)

def menu():
	menu_ = {'1':imprimeAyuda, '2':calcDeterminante}
	option = input("test> ")

	f = menu_.get(option, None)
	if f:
		f()
 
	return option == "0"

@numba.jit
def rellenaMatriz(x):
	return numpy.random.uniform(-10.0, 10.0, size=(x,x));

def calcDeterminante():
	interprete_ = []
	numba_      = []

	for x in range(90,501,10):
		m = rellenaMatriz(x)

		print(x, "elementos.")

		# Interprete
		start_time   = time()
		a.determinante(m, x)
		interprete_.append(time() - start_time)

		# Numba
		start_time   = time()
		a.determinanteNumba(m, x)
		numba_.append(time() - start_time)

	escribeFichero(interprete_, "determinante_interprete")
	escribeFichero(numba_, "determinante_numba")
