#ifndef DETERMINATERECURSIVO_H
#define DETERMINATERECURSIVO_H

#include "../funciones/funciones.h"

/**
 * Inicia el proceso para ajustar la función polinomica del determinante iterativo.
 */
void determinanteRecursivo();
/**
 * Ejecuta el algoritmo de ordenación para cada uno de los tamaños de vector y calcula el tiempo medio para las repeticiones.
 * @param min           Tamaño mínimo del vector.
 * @param max           Tamaño máximo del vector.
 * @param incremento    El orden de la matriz se incrementa de x en x.
 * @param tiemposReales Vector para almacenar el tiempo.
 * @param nElementos    Vector para almacenar el tamaño de vector.
 */
void tiempoDeterminanteRecursivo(
	int min, 
	int max, 
	int incremento,
	vector<double> &tiemposReales, 
	vector<double> &nElementos
);

/**
 * Calcula el determinante de una matriz de orden n de forma recursiva.
 * @param  M Matriz.
 * @param  n Orden de la matriz.
 * @return   Determinante para poder comprobar si funciona de forma correnta.
 */
double calcularDeterminanteRecursivo(vector <vector <double>> &M, int n);

#endif