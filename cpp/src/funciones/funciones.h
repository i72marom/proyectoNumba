#ifndef FUNCIONES_H
#define FUNCIONES_H

#include <fstream>
#include <string>
#include <vector>
#include "../classTime/classTime.h"

using namespace std;

/**
 * Rellena la matriz de forma aleatoria con valores de tipo double de entre 0.95 y 1.05.
 * @param M Matriz a rellenar.
 */
void rellenarMatriz(vector<vector <double>> &M);

/**
 * Guarda los datos en un fichero para poder generar la gráfica.
 * @param tReal     Vector de tiempos reales.
 * @param tEstimado Vector de tiempos estimados.
 * @param nElements Vector con el tamaño de los vectores estimados.
 * @param nombre    Nombre del fichero.
 */
void escribeFichero(
	vector<double> &tReal, 
	vector<double> &nElements,
	string nombre
);

#endif