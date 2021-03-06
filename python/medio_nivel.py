from algoritmos import *
from time import time
import random
import os.path as p

def preguntaGuardar(lista):
	option = input("Pulsa s para guardar: ")

	if option.lower() == "s":
		path = input("Nombre del archivo (se guarda en txt/): ")
		if p.isfile("txt/" + path + ".txt"): 
			option = input("txt/" + path + ".txt ya existe. Pulsa s para sobreescribir: ")
		
		if option.lower() == "s": 
			escribeFichero(lista, path)
			print("Guardando...")


def escribeFichero(lista, nombre):
	f = open("txt/" + nombre + ".txt", "w")
	
	# numero de elementos, tiempo interprete, tiempo numba
	for i in lista: 
		f.write(str(i[0]) + " "+ str('{:,.15f}'.format(i[1])) + " "+ str('{:,.15f}'.format(i[2])) + "\n")

	f.close()

def imprimeAyuda():
	ayuda_ = "Opciones: \n\t0. Salir. \n\t1. Muestra este menú. \n\t2. Determinante iterativo.\n\t3. Determinante recursivo.\n\t4. Exponente de una matriz.\n"
	print(ayuda_)

def menu():
	menu_ = {'2', '3', '4'}
	option = input("test> ")

	if option == "1": imprimeAyuda()
	elif option in menu_: calcularTiempos(option)
	else: return option == "0"

@numba.jit
def rellenaMatriz(x):
	return numpy.random.uniform(1.0, 5.0, size=(x,x));

def calcularTiempos(option):
	alg_iterativos_ = {'2':determinanteIter, '3':detRecursivo, '4':exponenteMatriz}
	alg_numba_      = {'2':determinanteIterNumba, '3':detRecursivoNumba, '4':exponenteMatrizNumba}
	datos           = []

	f1 = alg_iterativos_.get(option, None)
	f2 = alg_numba_.get(option, None)

	if f1 and f2:
		min_ = int(input("Numero minimo de elementos: "))
		max_ = int(input("Numero maximo de elementos: "))
		i    = int(input("Intervalo: "))

		for x in range(min_,max_+1,i):
			m = rellenaMatriz(x)

			# interprete
			start_time = time()
			f1(m, x)
			tiempo_int = time() - start_time

			#numba
			start_time = time()
			f2(m, x)
			tiempo_numba = time() - start_time

			print(x, "elementos.", "Interprete:", '{:,.15f}'.format(tiempo_int), "segundos. Numba:", '{:,.15f}'.format(tiempo_numba), "segundos.")
			datos.append([x, tiempo_int, tiempo_numba])

	preguntaGuardar(datos)
