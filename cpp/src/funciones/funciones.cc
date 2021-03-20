#include "funciones.h"

void escribeFichero(vector<double> &tReal, vector<double> &nElements, string nombre) {
	ofstream f(nombre);

	for (int i = 0; i < nElements.size(); ++i) {
		f << nElements[i] << " " << tReal[i] << endl;
	}

	f.close();
}

void rellenarMatriz(vector<vector <double>> &M) {
	for (auto &i : M) {
		for (auto &v : i)
			v = 0.95 + (double(rand() % 10)) / 100;
	}
}
