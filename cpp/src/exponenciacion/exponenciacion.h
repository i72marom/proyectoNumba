#ifndef EXP_H
#define EXP_H

#include <fstream>
#include <string>
#include <vector>
#include "../classTime/classTime.h"
#include "../funciones/funciones.h"

using namespace std;

/**
 * Calcula el producto de dos matrices de orden n.
 * @param A         Primera matriz.
 * @param B         Segunda matriz.
 * @param resultado Resultado del producto.
 */
void productoMatriz(
	vector<vector<double>> &A, 
	vector<vector<double>> &B,
	vector<vector<double>> &resultado
);

void expMatriz();

void tiemposExponenciacion(int min, int max, int inc, int exp);

void exponenciacion(vector<vector<double>> M, int o, int exp);

#endif