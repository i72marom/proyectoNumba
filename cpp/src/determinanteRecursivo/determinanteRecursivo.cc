#include "determinanteRecursivo.h"

void determinanteRecursivo() {
	vector<double> tiemposReales, nElementos;
	int max, min, incremento;

	cout << "Número mínimo de elementos: ";
	cin >> min;
	cout << "Número máximo de elementos: ";
	cin >> max;
	cout << "Incremento: ";
	cin >> incremento;

	tiempoDeterminanteRecursivo(min, max, incremento, tiemposReales, nElementos);
	escribeFichero(tiemposReales, nElementos, "../text/recursivo.txt");
}

void tiempoDeterminanteRecursivo(int min, int max, int incremento,
vector<double> &tiemposReales, vector<double> &nElementos) {
	vector<vector <double>> M;
	Clock Tiempo;
	double det;

	for (int i = min; i <= max; i += incremento) {
		M = vector <vector <double>>(i, vector <double>(i));
		rellenarMatriz(M);

		Tiempo.start();
		det = calcularDeterminanteRecursivo(M, i);

		if (Tiempo.isStarted()) Tiempo.stop();

		tiemposReales.push_back(Tiempo.elapsed() * 0.000001);
		nElementos.push_back(i);

		cout << nElementos.back() << " ";
		cout << tiemposReales.back() << " ";
		cout << det << endl;
	}
}

double calcularDeterminanteRecursivo(vector <vector <double>> &M, int n) {
	if (n == 1) return M[0][0];
	
	int f = 1;
	double det = 0;

	for (int i=0; i < n; i++) {
		vector <vector <double>> submatriz(n-1, vector <double>(n-1));
		
		for (int j = 0; j < n-1; j++) {
			
			for (int k = 0; k < n-1; k++) {
				if (k < i)  submatriz[j][k] = M[j+1][k];
				if (k >= i) submatriz[j][k] = M[j+1][k+1];
			}
		}

		det += f * M[0][i] * calcularDeterminanteRecursivo(submatriz, n-1);
		f *= -1;
	}

	return det;
}
