import numpy
import numba
from time import time
from algoritmos import *
import random

def escribeFichero(lista, nombre):
	f = open("txt/" + nombre + ".txt", "w")
	
	for i in lista: 
		f.write(str('{:,.15f}'.format(i)) + "\n")

	f.close()

def imprimeAyuda():
	ayuda_ = "Opciones: \n\t0. Salir. \n\t1. Ayuda. \n\t2. Determinante iterativo.\n\t3. Determinante recursivo.\n"
	print(ayuda_)

def menu():
	menu_ = {'2', '3'}
	option = input("test> ")

	if option == "1": imprimeAyuda()
	elif option in menu_: calcularTiempos(option)
	else: return option == "0"

@numba.jit
def rellenaMatriz(x):
	return numpy.random.uniform(-10.0, 10.0, size=(x,x));

def calcularTiempos(option):
	alg_iterativos_ = {'2':determinanteIter, '3':detRecursivo}
	alg_numba_      = {'2':determinanteIterNumba, '3':detRecursivoNumba}
	datos     = []

	f1 = alg_iterativos_.get(option, None)
	f2 = alg_numba_.get(option, None)
	if f1 and f2:
		max_ = input("Numero maximo de elementos: ")
		min_ = input("Numero minimo de elementos: ")
		i = input("Intervalo: ")

		for x in range(min_,max_,i):
			m = rellenaMatriz(x)

			print(x, "elementos.")

			# interprete
			start_time = time()
			f1(m, x)
			tiempo_int = time() - start_time

			#numba
			start_time = time()
			f2(m, x)
			tiempo_numba = time() - start_time

			datos.append([x, tiempo_int, tiempo_numba])

#	escribeFichero(interprete_, str(f))
